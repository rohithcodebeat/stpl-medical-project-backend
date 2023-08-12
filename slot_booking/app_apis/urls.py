from django.urls import path
from . import views

urlpatterns=[
    path('slot-list-api/<doc_id>/',views.AppAPIsOrganisationSlotBookingModelSlotListAPIView.as_view(),name='AppAPIsOrganisationSlotBookingModelSlotListAPIView'),
    
]