from django.urls import path
from . import views

urlpatterns =[
    
    path('organisation-list-api/',views.AppAPIsOrganisationModelDiagnosisListAPIView.as_view(),name='AppAPIsOrganisationModelDiagnosisListAPIView'),
    
]