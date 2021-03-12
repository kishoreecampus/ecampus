from rest_framework import serializers
from preadmission.models import Application
from student.models import Document
from student.serializers import StudentApplicationDocumentSerializer
from django.conf import settings

class ApplicationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        exclude = ['is_verified', 'created_on', 'created_by', 'reference_number', 'is_applied', 'docs', 'application_token']

    def validate(self, validate_data):
        if not validate_data[validate_data['primary_contact_person']+"_mobile"]:
            raise serializers.ValidationError({'primary_contact_person':"Required " + validate_data['primary_contact_person'] +" mobile number"})
        return validate_data

class ApplicationUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        exclude = ('created_on', 'created_by', 'is_applied', 'is_docs_verified', 'docs', 'query')
    
    def validate(self, validate_data):
        if self.instance.is_verified:
            raise serializers.ValidationError({"is_verified":"Already this enquiry application has been verified."})
        if not validate_data[validate_data['primary_contact_person']+"_mobile"]:
            raise serializers.ValidationError({'primary_contact_person':"Required " + validate_data['primary_contact_person'] +" mobile number"})
        return validate_data

class ApplicationListSerializer(serializers.ModelSerializer):    

    class Meta:
        model = Application
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        document_object = StudentApplicationDocumentSerializer(instance.docs).data
        if document_object.get('student_photo'):
            document_object['student_photo'] = "{0}?token={1}&ref={2}&target={3}&dir={4}".format(document_object.get('student_photo'), instance.application_token, instance.reference_number, 'student_photo', 'documents')
        if document_object.get('birth_certificate'):
            document_object['birth_certificate'] = "{0}?token={1}&ref={2}&target={3}&dir={4}".format(document_object.get('birth_certificate'), instance.application_token, instance.reference_number, 'birth_certificate', 'documents')
        if document_object.get('tc'):
            document_object['tc'] = "{0}?token={1}&ref={2}&target={3}&dir={4}".format(document_object.get('tc'), instance.application_token, instance.reference_number, 'tc', 'documents')
        response['documents'] = document_object
        return response

class SubmitApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ['id', 'docs']

    def validate(self, validate_data):
        if not self.instance.is_verified:
            raise serializers.ValidationError({"is_verified":"Enquiry application not yet verified."})
        if self.instance.is_applied and not self.instance.is_docs_verified:
            raise serializers.ValidationError({"is_applied":"Already the application documents submitted and waiting for verify."})
        if self.instance.is_applied and self.instance.is_docs_verified:
            raise serializers.ValidationError({"is_applied":"Already the application documents submitted and it is approved."})
        required_keys = ['student_photo', 'birth_certificate']
        if hasattr(self, 'initial_data'):
            extra_keys = set(self.initial_data.keys()) - set(self.fields.keys())
            if extra_keys:
                for key in required_keys:
                    if not key in extra_keys:
                        raise serializers.ValidationError("required " + key)
            else:
                raise serializers.ValidationError("Required Photo, Birth certificate, TC")
        # raise serializers.ValidationError("Required Photo, Birth certificate, TC ccc")
        return validate_data

class ApproveOrRejectDocSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ['id', 'is_docs_verified', 'query']

    def validate(self, validate_data):
        if validate_data['is_docs_verified'] == False and not validate_data['query']:
            raise serializers.ValidationError({"query":"Please enter rejection reason."})
        if not self.instance.is_verified:
            raise serializers.ValidationError({"is_verified":"Enquiry application not yet verified."})
        if not self.instance.is_applied:
            raise serializers.ValidationError({"is_applied":"Documents not yet submitted."})
        if self.instance.is_docs_verified:
            raise serializers.ValidationError({"is_docs_verified":"Documents already verified."})
        return validate_data