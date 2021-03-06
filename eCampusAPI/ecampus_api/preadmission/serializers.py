from rest_framework import serializers
from preadmission.models import Application
from student.models import Document
from student.serializers import StudentDocumentSerializer

class ApplicationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        exclude = ['is_verified', 'created_on', 'created_by', 'reference_number', 'is_applied']

    def validate(self, validate_data):
        if validate_data['student_name'] and not validate_data['student_name'].isalpha():
            raise serializers.ValidationError("Invalid student name")
        if validate_data['father_name'] and not validate_data['father_name'].isalpha():
            raise serializers.ValidationError("Invalid father name")
        if validate_data['father_mobile']:
            if not validate_data['father_mobile'].isnumeric() or len(str(validate_data['father_mobile'])) != 10:
                raise serializers.ValidationError("Invalid father mobile")
        if validate_data['mother_name'] and not validate_data['mother_name'].isalpha():
            raise serializers.ValidationError("Invalid mother name")
        if validate_data['mother_mobile']:
            if not validate_data['mother_mobile'].isnumeric() or len(str(validate_data['mother_mobile'])) != 10:
                raise serializers.ValidationError("Invalid mother mobile")
        if len(str(validate_data['post_code'])) != 6:
            raise serializers.ValidationError("Invalid post code")
        if validate_data['guardian_name'] and not validate_data['guardian_name'].isalpha():
            raise serializers.ValidationError("Invalid guardian name")
        if  validate_data['guardian_mobile']:
            if not validate_data['guardian_mobile'].isnumeric() or len(str(validate_data['guardian_mobile'])) != 10:
                raise serializers.ValidationError("Invalid guardian mobile")
        if validate_data['guardian_post_code']:
            if len(str(validate_data['guardian_post_code'])) != 6:
                raise serializers.ValidationError("Invalid guardian post code")
        return validate_data

    # def create(self, validate_data):
    #     enquiry = Enquiry.objects.create(**validate_data)
    #     enquiry.created_by = self.request.user.id
    #     return enquiry

class ApplicationUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        exclude = ('created_by', 'is_applied')
    
    def validate(self, validate_data):
        if self.instance.is_verified:
            raise serializers.ValidationError("Already this enquiry application has been verified.")
        if validate_data['student_name'] and not validate_data['student_name'].isalpha():
            raise serializers.ValidationError("Invalid student name")
        if validate_data['father_name'] and not validate_data['father_name'].isalpha():
            raise serializers.ValidationError("Invalid father name")
        if validate_data['father_mobile']:
            if not validate_data['father_mobile'].isnumeric() or len(str(validate_data['father_mobile'])) != 10:
                raise serializers.ValidationError("Invalid father mobile")
        if validate_data['mother_name'] and not validate_data['mother_name'].isalpha():
            raise serializers.ValidationError("Invalid mother name")
        if validate_data['mother_mobile']:
            if not validate_data['mother_mobile'].isnumeric() or len(str(validate_data['mother_mobile'])) != 10:
                raise serializers.ValidationError("Invalid mother mobile")
        if len(str(validate_data['post_code'])) != 6:
            raise serializers.ValidationError("Invalid post code")
        if validate_data['guardian_name'] and not validate_data['guardian_name'].isalpha():
            raise serializers.ValidationError("Invalid guardian name")
        if  validate_data['guardian_mobile']:
            if not validate_data['guardian_mobile'].isnumeric() or len(str(validate_data['guardian_mobile'])) != 10:
                raise serializers.ValidationError("Invalid guardian mobile")
        if validate_data['guardian_post_code']:
            if len(str(validate_data['guardian_post_code'])) != 6:
                raise serializers.ValidationError("Invalid guardian post code")
        if not validate_data[validate_data['primary_contact_person']+"_mobile"]:
            raise serializers.ValidationError("Required " + validate_data['primary_contact_person'] +" mobile number")
        if validate_data[validate_data['primary_contact_person']+"_mobile"]:
            if not validate_data[validate_data['primary_contact_person']+"_mobile"].isnumeric() or len(str(validate_data[validate_data['primary_contact_person']+"_mobile"])) != 10:
                raise serializers.ValidationError("Invalid "+ validate_data['primary_contact_person'] +" mobile")
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