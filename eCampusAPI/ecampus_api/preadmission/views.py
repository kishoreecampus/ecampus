from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from preadmission import serializers
from preadmission.models import Application
from api_authentication.permissions import HasOrganizationAPIKey
from rest_framework.permissions import AllowAny, IsAuthenticated
from employee.permissions import EmployeeHasPermission
from datetime import datetime
import time
from base.views import send_sms, MultipleFieldLookupMixin
from student.models import Document
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
import secrets
import hashlib

class ApplicationMixin(viewsets.ModelViewSet):
    
    queryset = Application.objects.all()
    serializer_class = serializers.ApplicationCreateSerializer

    def get_reference_numer(self):
        # reference_number = str(datetime.now()).split(".")[0].replace("-","").replace(" ","").replace(":","")
        # act_number = reference_number[2:len(reference_number)]
        return str(time.time()).replace(".","")

    def unique_token(self):
        salt = secrets.token_hex(8)   + self.get_reference_numer()
        unique_token = hashlib.sha256(salt.encode('utf-8')).hexdigest()
        return unique_token

class ApplicationViewSet(ApplicationMixin):
    
    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.ApplicationCreateSerializer
        if self.action == 'update':
            return serializers.ApplicationUpdateSerializer
        if self.action == 'list':
            return serializers.ApplicationListSerializer
        if self.action == 'retrieve':
            return serializers.ApplicationListSerializer
        return super(serializers.ApplicationCreateSerializer, self).get_serializer_class()

    def get_permissions(self):
        if self.action == 'create' or self.action == 'retrieve':
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()

    def get_queryset(self):
        if self.action == 'retrieve':
            return Application.objects.filter(application_token=self.request.GET.get('application_token', None))
        return super().get_queryset()

    def perform_create(self, serializer):
        unique_token = self.unique_token()
        if self.request.user.is_authenticated:
            user  = self.request.user.id
        else:
            user = 0
        serializer.save(application_token=unique_token, created_by=user)

    def perform_update(self, serializer):
        enquiry_reference_numer = None
        is_verified = self.request.data.get('is_verified')
        if is_verified == True:
            enquiry_reference_numer = self.get_reference_numer()
            mobile_number = self.request.data[self.request.data['primary_contact_person']+"_mobile"]
            message = "Application link - " + str(enquiry_reference_numer)
            # send_sms(mobile_number, message)
        serializer.save(reference_number=enquiry_reference_numer)

class SubmitDocsViewSet(MultipleFieldLookupMixin, ApplicationMixin):
    lookup_fields = ('id', 'application_token')
    serializer_class = serializers.SubmitApplicationSerializer
    # parser_classes = [FormParser, MultiPartParser,]
    permission_classes = [AllowAny, HasOrganizationAPIKey]

    def get_permissions(self):
        if self.action == 'update':
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()

    def perform_update(self, serializer):
        student_photo = self.request.FILES.get('student_photo', None)
        birth_certificate = self.request.FILES.get('birth_certificate', None)
        tc = self.request.FILES.get('tc', None)
        photo = self.request.FILES.get('photo', None)
        request_documents = {}
        if self.get_object().is_verified:
            if self.get_object().docs:
                doc_id = self.get_object().docs.id
            else:
                doc_id = None
            if student_photo:
                request_documents['student_photo'] = student_photo
            if birth_certificate:
                request_documents['birth_certificate'] = birth_certificate
            if tc:
                request_documents['tc'] = tc
            if photo:
                request_documents['photo'] = photo
            obj, student_document = Document.objects.update_or_create(id=doc_id, defaults=request_documents)
            application_instance = serializer.save(docs=obj, is_applied=True)

class ApproveOrRejectDoc(MultipleFieldLookupMixin, ApplicationMixin):
    lookup_fields = ('id', 'application_token')
    serializer_class = serializers.ApproveOrRejectDocSerializer

    def perform_update(self, serializer):
        is_docs_verified = self.request.data.get('is_docs_verified')
        self_obj = self.get_object()
        if is_docs_verified == False and self_obj.is_applied == True:
            unique_token = self.unique_token()
            contact_person = self_obj.primary_contact_person
            contact_number = getattr(self_obj, contact_person + "_mobile")
            message = "Application link - " + str(unique_token)
            send_sms(contact_number, message)
            serializer.save(is_applied=False, application_token=unique_token)
        else:
            serializer.save(is_docs_verified=True)