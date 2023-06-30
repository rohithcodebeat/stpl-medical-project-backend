from django.urls import path, include 

urlpatterns = [
    path("app/apis/", include("organisation.app_apis.urls")),
    
]
