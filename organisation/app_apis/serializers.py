from rest_framework import serializers
from ..models import CategoryModel,OrganisationMediaGalleryModel,OrganisationModel,OrganisationCategoryDescriptionModel,OrganisationCategoryModel,OrganisationDoctorModel
from address.app_apis.serializers import AppAPIsAddressModelListSerializer
from userprofile.models import UserProfileModel

class AppAPIsOrganisationCategoryDescriptionModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganisationCategoryDescriptionModel
        fields=['description']

class AppAPIsOrganisationDoctorModelListSerializer(serializers.ModelSerializer):
    doctor=serializers.SerializerMethodField()
    profile=serializers.SerializerMethodField()
    class Meta:
        model=OrganisationDoctorModel
        fields=['id','doctor','profile','price','is_fasting','category']

    def get_doctor(self,obj):
        try:
            data=obj.user.username
        except:
            data={}
        return data
    
    def get_profile(self,obj):
        try:
            user=UserProfileModel.objects.get(user=obj.user)
            data=user.profile_pics
        except:
            data=""
        return data

class AppAPIsOrganisationCategoryModelListSerializer(serializers.ModelSerializer):
    multipleTestList=serializers.SerializerMethodField()
    organisation_doctor=serializers.SerializerMethodField()

    class Meta:
        model=OrganisationCategoryModel
        fields=['id','title','multipleTestList','organisation_doctor']

    def get_multipleTestList(self,obj):
        try:
            data=AppAPIsOrganisationCategoryDescriptionModelListSerializer(obj.description.all(),many=True).data
        except:
            data=[]
        return data

    def get_organisation_doctor(self, obj):
        try:
            data=AppAPIsOrganisationDoctorModelListSerializer(obj.OrganisationDoctorModel_category.all(),many=True).data
        except:
            data=[]
        return data


class AppAPIsOrganisationModelListSerializer(serializers.ModelSerializer):
    address=serializers.SerializerMethodField()
    tests=serializers.SerializerMethodField()
    icon=serializers.SerializerMethodField()

    class Meta:
        model=OrganisationModel
        fields=['id','title','sub_title','profile','icon','address','tests']

    def get_address(self,obj):
        try:
            data=AppAPIsAddressModelListSerializer(obj.address,many=False).data
        except:
            data={}
        return data
    
    def get_tests(self,obj):
        try:
            data=AppAPIsOrganisationCategoryModelListSerializer(obj.OrganisationCategoryModel_organisation.all(),many=True).data
        except:
            data=[]
        return data

    def get_icon(self, obj):
        try:
            data=obj.icon.media
        except:
            data=""
        return data
