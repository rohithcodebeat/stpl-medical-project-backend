from django.urls import path, include 

urlpatterns = [
    path("app/apis/", include("slot_booking.app_apis")),
]
