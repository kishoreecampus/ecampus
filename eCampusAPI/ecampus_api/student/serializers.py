from rest_framework import serializers
from student.models import StudentDocument

class StudentDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentDocument
        # fields = '__all__'
        exclude = ['uploaded_on', ]