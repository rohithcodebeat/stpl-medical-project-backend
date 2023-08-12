from rest_framework import serializers
from ..models import UserCartModel,UserProfileMediaGalleryModel,UserProfileModel
from slot_booking.models import OrganisationSlotBookingModel
from slot_booking.app_apis.serializers import AppAPIsOrganisationSlotBookingModelListSerializer

class AppAPIsUserCartModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserCartModel
        fields="__all__"
        
class AppAPIsUserCartModelListSerializer(serializers.ModelSerializer):
    slots=serializers.SerializerMethodField()
    # total=serializers.SerializerMethodField()
    
    class Meta:
        model=UserCartModel
        fields=['id','slots']
    
    def get_slots(self,obj):
        try:
            data=AppAPIsOrganisationSlotBookingModelListSerializer(obj.slot.all(),many=True).data
        except:
            data=[]
        return data

    # def get_total(self,obj):
    #     try:
    #         slots=obj.slot.all()
    #         data=0
    #         for slot in slots:
    #             data+=slot.doctor.price
            
    #     except:
    #         data=0
    #     return data

    