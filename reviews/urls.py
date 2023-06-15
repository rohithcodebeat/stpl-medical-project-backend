from django.urls import path, include 

urlpatterns = [
    path("app/apis/", include("reviews.app_apis")),
]
