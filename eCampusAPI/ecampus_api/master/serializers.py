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


    def validate(self, validated_data):
        if validated_data['trust_name'] and not validated_data['trust_name'].isalpha():
            raise serializers.ValidationError("Invalid trust name")
        if validated_data['institution_name'] and not validated_data['institution_name'].isalpha():
            raise serializers.ValidationError("Invalid institution name")
        if Profile.objects.filter(trust_name=validated_data['trust_name']).exists():
            raise serializers.ValidationError('trust name already exist.')
        if Profile.objects.filter(mobile_number=validated_data['mobile_number']).exists():
            raise serializers.ValidationError('mobile number already exist.')
        if Profile.objects.filter(institution_name=validated_data['institution_name']).exists():
            raise serializers.ValidationError('institution name already exist.')
        if Profile.objects.filter(phone_number=validated_data['phone_number']).exists():
                raise serializers.ValidationError('phone number already exist.')
        return validated_data
              

class ProfileUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['trust_name', 'institution_name','address1','address2','phone_number','administrator','mobile_number']

    def validate(self, validated_data):
        if is_superuser_id(self.instance.id):
                raise serializers.ValidationError('You do not have permission')
        if validated_data['trust_name'] and not validated_data['trust_name'].isalpha():
            raise serializers.ValidationError("Invalid trust name")
        if validated_data['institution_name'] and not validated_data['institution_name'].isalpha():
            raise serializers.ValidationError("Invalid institution name")
        if Profile.objects.filter(trust_name=validated_data['trust_name']).exists():
            raise serializers.ValidationError('trust name already exist.')
        if Profile.objects.filter(mobile_number=validated_data['mobile_number']).exists():
            raise serializers.ValidationError('mobile number already exist.')
        if Profile.objects.filter(institution_name=validated_data['institution_name']).exists():
            raise serializers.ValidationError(
                'institution name already exist.')
        if Profile.objects.filter(phone_number=validated_data['phone_number']).exists():
            raise serializers.ValidationError('phone number already exist.')
        return validated_data

class ProfileDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['id', 'trust_name', 'institution_name','address1','address2','phone_number','administrator','mobile_number','created_on','created_by']
    
    def validate(self, validated_data):
        if is_superuser_id(self.instance.id):
            raise serializers.ValidationError('You do not have permission')
        return validated_data

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
    
    def validate(self, validated_data):
        if ClassGroup.objects.filter(class_group=validated_data['class_group']).exists():
            raise serializers.ValidationError('class group already exist.')
    
        if validated_data['class_group'] and not validated_data['class_group'].isalpha():
            raise serializers.ValidationError("Invalid class group name")
    
        return validated_data 


class ClassGroupUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClassGroup
        fields = ['class_group','created_on'] 

    def validate(self, validated_data):
        if is_superuser_id(self.instance.id):
            raise serializers.ValidationError('You do not have permission')
        if validated_data['class_group'] and not validated_data['class_group'].isalpha():
            raise serializers.ValidationError("Invalid class group name")
        if ClassGroup.objects.filter(class_group=validated_data['class_group']).exists():
            raise serializers.ValidationError('class group already exist.')
        return validated_data


class ClassGroupDetailSerializer(serializers.ModelSerializer): 

    class Meta:
        model = ClassGroup
        fields = ['id','class_group','created_on','created_by']

    def validate(self, validated_data):
        if is_superuser_id(self.instance.id):
            raise serializers.ValidationError('You do not have permission')
        return validated_data 


class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = ['id','class_group','class_name']



class ClassNameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = ['class_group','class_name']

    def validate(self, validated_data):
        if ClassName.objects.filter(class_name=validated_data['class_name']).exists():
            raise serializers.ValidationError('class name already exist.')
        if validated_data['class_name'] and not validated_data['class_name'].isalpha():
            raise serializers.ValidationError("Invalid class name")

        if validated_data['class_name'] and not validated_data['class_name'].islower():
            raise serializers.ValidationError("Invalid class name")
        return validated_data


class ClassNameUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = ['class_group','class_name','created_on']
    
    def validate(self, validated_data):
        if is_superuser_id(self.instance.id):
            raise serializers.ValidationError('You do not have permission')
        if ClassName.objects.filter(class_name=validated_data['class_name']).exists():
            raise serializers.ValidationError('class name already exist.')
        if validated_data['class_name'] and not validated_data['class_name'].isalpha():
            raise serializers.ValidationError("Invalid class name")

        if validated_data['class_name'] and not validated_data['class_name'].islower():
            raise serializers.ValidationError("Invalid class name")
        return validated_data

class ClassNameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = ['id','class_group','class_name','created_on','created_by']

    def validate(self, validated_data):
        if is_superuser_id(self.instance.id):
            raise serializers.ValidationError('You do not have permission')
        return validated_data

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id','class_name','section_name']



class SectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['class_name','section_name']

    def validate(self,validated_data):
        if Section.objects.filter(section_name=validated_data['section_name']).exists():
            raise serializers.ValidationError('section name already exist.')
        if validated_data['section_name'] and not validated_data['section_name'].isalnum():
            raise serializers.ValidationError("Invalid section name")
        if validated_data['section_name'] and not validated_data['section_name'].islower():
            raise serializers.ValidationError("Invalid section name")
        return validated_data



class SectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['class_name', 'section_name', 'created_on']
    
    def validate(self, validated_data):
            if is_superuser_id(self.instance.id):
                raise serializers.ValidationError('You do not have permission')
            return validated_data

class SectionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'class_name', 'section_name',
                  'created_on', 'created_by']
    
    def validate(self, validated_data):
            if is_superuser_id(self.instance.id):
                raise serializers.ValidationError('You do not have permission')
            return validated_data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']  


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']

    def validate(self,validated_data):
        if Category.objects.filter(category=validated_data['category']).exists():
            raise serializers.ValidationError('Category already exists')
        if validated_data['category'] and not validated_data['category'].isalnum():
            raise serializers.ValidationError("Invalid category")

        return validated_data


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category', 'created_on']

    def validate(self, validated_data):
            if is_superuser_id(self.instance.id):
                raise serializers.ValidationError('You do not have permission')
            return validated_data


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category','created_on', 'created_by']

    def validate(self, validated_data):
            if is_superuser_id(self.instance.id):
                raise serializers.ValidationError('You do not have permission')
            return validated_data

class CasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caste
        fields = ['category', 'caste']

class CasteCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Caste
        fields = ['category', 'caste']
    
    def validate(self,validated_data):
        if Caste.objects.filter(caste=validated_data['caste']).exists():
            raise serializers.ValidationError('Caste already exists')
        if validated_data['caste'] and not validated_data['caste'].isalpha():
            raise serializers.ValidationError("Invalid Caste")
        return validated_data
    
class CasteUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Caste
        fields = ['category', 'caste', 'created_on']

    def validate(self, validated_data):
        if is_superuser_id(self.instance.id):
            raise serializers.ValidationError('You do not have permission')
        return validated_data


class CasteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caste
        fields = ['id', 'category', 'caste', 'created_on', 'created_by']

    def validate(self, validated_data):
            if is_superuser_id(self.instance.id):
                raise serializers.ValidationError('You do not have permission')
            return validated_data
