from rest_framework import serializers
from ..models import OrganisationSlotBookingModel

class AppAPIsOrganisationSlotBookingModelListSerializer(serializers.ModelSerializer):
    org_id=serializers.SerializerMethodField()
    test_id=serializers.SerializerMethodField()
    test_name=serializers.SerializerMethodField()
    price=serializers.SerializerMethodField()
    time=serializers.SerializerMethodField()
    report_availability=serializers.SerializerMethodField()

    class Meta:
        model=OrganisationSlotBookingModel
        fields=['id','org_id','test_id','test_name','time','price','report_availability']

    def get_org_id(self,obj):
        try:
            data=obj.doctor.category.organisation.id
        except:
            data=None
        return data
    
    def get_test_id(self,obj):
        try:
            data=obj.doctor.category.id
        except:
            data=None
        return data

    def get_test_name(self,obj):
        try:
            data=obj.doctor.category.title
        except:
            data=""
        return data

    def get_time(self,obj):
        try:
            data=obj.start_datetime
            # data=str(obj.start_datetime.hour)+":"
            # if obj.start_datetime.minute==0:
            #     data+="00"
            # else:
            #     data+=str(obj.start_datetime.minute)
        except:
            data=""
        return data

    def get_price(self,obj):
        try:
            data=obj.doctor.price
        except:
            data=""
        return data

    def get_report_availability(self,obj):
        return 2

class AppAPIsOrganisationSlotBookingModelSlotListSerializer(serializers.ModelSerializer):
    start_time=serializers.SerializerMethodField()
    end_time=serializers.SerializerMethodField()
    class Meta:
        model=OrganisationSlotBookingModel
        fields=['id','date','start_time','end_time','status','is_booked']

    def get_start_time(self,obj):
        try:
            data=str(obj.start_datetime.hour)+":"
            if obj.start_datetime.minute==0:
                data+="00"
            else:
                data+=str(obj.start_datetime.minute)
        except:
            data=""
        return data

    def get_end_time(self,obj):
        try:
            data=str(obj.end_datetime.hour)+":"
            if obj.end_datetime.minute==0:
                data+="00"
            else:
                data+=str(obj.end_datetime.minute)
        except:
            data=""
        return data