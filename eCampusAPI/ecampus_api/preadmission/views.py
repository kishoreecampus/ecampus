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
from base.views import send_sms
from student.models import Document
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

class ApplicationMixin(viewsets.ModelViewSet):
    
    queryset = Application.objects.all()
    serializer_class = serializers.ApplicationCreateSerializer

    def get_reference_numer(self):
        # reference_number = str(datetime.now()).split(".")[0].replace("-","").replace(" ","").replace(":","")
        # act_number = reference_number[2:len(reference_number)]
        return str(time.time()).replace(".","")

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
        if self.action == 'create':
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            user  = self.request.user.id
        else:
            user = 0
        serializer.save(created_by=user)

    def perform_update(self, serializer):
        enquiry_reference_numer = None
        is_verified = self.request.data.get('is_verified')
        if is_verified == True:
            enquiry_reference_numer = self.get_reference_numer()
            mobile_number = self.request.data[self.request.data['primary_contact_person']+"_mobile"]
            message = "Application link - " + str(enquiry_reference_numer)
            # send_sms(mobile_number, message)
        serializer.save(reference_number=enquiry_reference_numer)


class SubmitApplicationViewSet(ApplicationMixin):
    lookup_field = "reference_number"
    serializer_class = serializers.SubmitApplicationSerializer
    # parser_classes = [FormParser, MultiPartParser,]
    permission_classes = [AllowAny, HasOrganizationAPIKey]

    # def get_serializer_class(self):
    #     return serializers.SubmitApplicationSerializer

    def get_permissions(self):
        if self.action == 'update':
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()

    # def update(self, request, *args, **kwargs):
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_update(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         serializer.data
    #         return Response({"Success": "msb blablabla","data":serializer.data}, headers=headers)

    def perform_update(self, serializer):
        application_instance = serializer.save(is_applied = True)
        student_photo = self.request.FILES.get('student_photo', 'NULL')
        birth_certificate = self.request.FILES.get('birth_certificate', 'NUll')
        tc = self.request.FILES.get('tc', 'NULL')
        student_document = Document.objects.create(application=application_instance, student_photo=student_photo, birth_certificate=birth_certificate, tc=tc)
        student_document.save()
