from django.urls import path, include 

urlpatterns = [
    path("app/apis/", include("address.app_apis")),
]
