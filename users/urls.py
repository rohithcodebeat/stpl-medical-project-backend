from django.urls import path, include 

urlpatterns = [
    path("app/apis/", include("users.app_apis")),
]
