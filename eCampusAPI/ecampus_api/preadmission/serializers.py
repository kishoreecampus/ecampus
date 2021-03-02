from rest_framework import serializers
from preadmission.models import Application
from student.models import Document
from student.serializers import StudentDocumentSerializer

class ApplicationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        exclude = ['is_verified', 'created_on', 'created_by', 'reference_number', 'is_applied']

    def validate(self, validate_data):
        if not validate_data[validate_data['primary_contact_person']+"_mobile"]:
            raise serializers.ValidationError({'primary_contact_person':"Required " + validate_data['primary_contact_person'] +" mobile number"})
        return validate_data

class ApplicationUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        exclude = ('created_on', 'created_by', 'is_applied')
    
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

class SubmitApplicationSerializer(serializers.ModelSerializer):
    # student_document = StudentDocumentSerializer(many=True, read_only=False)
    # student_document = serializers.PrimaryKeyRelatedField(queryset=StudentDocument.objects.all())

    class Meta:
        model = Application
        # fields = ['studentdocument']
        exclude = ['id', 'query', 'is_verified', 'reference_number', 'created_by', 'is_applied']


    def validate(self, data):
        required_keys = ['student_photo', 'birth_certificate']
        if hasattr(self, 'initial_data'):
            extra_keys = set(self.initial_data.keys()) - set(self.fields.keys())
            if extra_keys:
                for key in required_keys:
                    if not key in extra_keys:
                        raise serializers.ValidationError("required " + key)
            else:
                raise serializers.ValidationError("Required Photo, Birth certificate, TC")
        return data