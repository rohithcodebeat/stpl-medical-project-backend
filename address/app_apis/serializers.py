from rest_framework import serializers
from ..models import CountryModel,StateModel,CityModel,AddressModel

class AppAPIsAddressModelListSerializer(serializers.ModelSerializer):
    city=serializers.SerializerMethodField()
    state=serializers.SerializerMethodField()
    country=serializers.SerializerMethodField()

    class Meta:
        model=AddressModel
        fields=['id','address_1','address_2','pincode','city','state','country']

    def get_city(self,obj):
        try:
            data=obj.city.title
        except:
            data=""
        return data

    def get_state(self,obj):
        try:
            data=obj.state.title
        except:
            data=""
        return data

    def get_country(self,obj):
        try:
            data=obj.country.title
        except:
            data=""
        return data

    
