from rest_framework import serializers
from .models import Profile,ClassGroup,ClassName,Section,RoomManagement,Category,Caste
from api_authentication.views import is_superuser_id
from rest_framework.validators import UniqueTogetherValidator


class ProfileSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Profile
        fields = ['id', 'trust_name', 'institution_name','address1','address2','phone_number','administrator','mobile_number']

class ProfileCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['trust_name', 'institution_name','address1','address2','phone_number','administrator','mobile_number']


              

class ProfileUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['trust_name', 'institution_name','address1','address2','phone_number','administrator','mobile_number']


class ProfileDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['id', 'trust_name', 'institution_name','address1','address2','phone_number','administrator','mobile_number','created_on','created_by']
    

class RoomManagementSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomManagement
        fields = ['id']

class ClassGroupSerializer(serializers.ModelSerializer): 

    class Meta:
        model = ClassGroup
        fields = ['id','class_group']


class ClassGroupCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClassGroup
        fields = ['class_group']
    



class ClassGroupUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClassGroup
        fields = ['class_group','created_on'] 



class ClassGroupDetailSerializer(serializers.ModelSerializer): 

    class Meta:
        model = ClassGroup
        fields = ['id','class_group','created_on','created_by']



class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = ['id','class_group','class_name']



class ClassNameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = ['class_group','class_name']




class ClassNameUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = ['class_group','class_name','created_on']
    


class ClassNameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = ['id','class_group','class_name','created_on','created_by']


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id','class_name','section_name']



class SectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['class_name','section_name']





class SectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['class_name', 'section_name', 'created_on']
    

class SectionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'class_name', 'section_name',
                  'created_on', 'created_by']  
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']  


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category', 'created_on']



class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category','created_on', 'created_by']


class CasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caste
        fields = ['category', 'caste']

class CasteCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Caste
        fields = ['category', 'caste']
    
    
class CasteUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Caste
        fields = ['category', 'caste', 'created_on']



class CasteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caste
        fields = ['id', 'category', 'caste', 'created_on', 'created_by']

