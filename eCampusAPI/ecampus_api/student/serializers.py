from rest_framework import serializers
from student.models import Document

class StudentDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        # fields = '__all__'
        exclude = ['uploaded_on', ]

class StudentApplicationDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        exclude = ['id', 'student']