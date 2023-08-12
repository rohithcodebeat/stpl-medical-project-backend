from rest_framework import generics,status
from rest_framework.response import Response
from ..models import UserCartModel,UserProfileModel,UserProfileMediaGalleryModel
from slot_booking.models import OrganisationSlotBookingModel
from .serializers import AppAPIsUserCartModelListSerializer,AppAPIsUserCartModelSerializer

class AppAPIsUserCartModelListAPIView(generics.ListAPIView):
    queryset=UserCartModel.objects.all()
    serializer_class=AppAPIsUserCartModelListSerializer
    
    def get(self, request):
        try:
            query = self.queryset.get(id=1)#later update = request.user.id
            serializer = self.serializer_class(query, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message" : f"something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)
        
class AppAPIsUserCartModelAddItemGenericAPIView(generics.GenericAPIView):
    # queryset=UserCartModel.objects.all()
    serializer_class=AppAPIsUserCartModelSerializer

    def post(self,request,id):
        try:
            user_cart=UserCartModel.objects.get(id=1)#later update = request.user.id
            slot_instance=OrganisationSlotBookingModel.objects.get(id=id)
            #to check if it is of same organisation
            slots=user_cart.slot.all()
            for slot in slots:
                if slot.doctor.category.organisation.id != slot_instance.doctor.category.organisation.id:
                    return Response({"message":"Different organisation slot is found"},status=status.HTTP_424_FAILED_DEPENDENCY)
            if user_cart.slot.filter(id=slot_instance.id).exists():
                return Response({"message" : "Already in the Cart"}, status=status.HTTP_200_OK)
            else:
                user_cart.slot.add(slot_instance)
                return Response({"message" : "Added Successfully"}, status=status.HTTP_200_OK)
            return Response({"message" : "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message" : f"something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)
        

class AppAPIsUserCartModelRemoveItemGenericAPIView(generics.GenericAPIView):
    serializer_class=AppAPIsUserCartModelSerializer

    def post(self,request,id):
        try:
            user_cart=UserCartModel.objects.get(id=1)#later update = request.user.id
            slot_instance=OrganisationSlotBookingModel.objects.get(id=id)
            if user_cart.slot.filter(id=slot_instance.id).exists():
                user_cart.slot.remove(slot_instance)
                return Response({"message" : "Removed Successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"message" : "Item Does not Exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message" : f"something went wrong, {e}"}, status=status.HTTP_400_BAD_REQUEST)
        
