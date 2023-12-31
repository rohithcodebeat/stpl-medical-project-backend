from rest_framework import generics,status,permissions
from rest_framework.response import Response
from .serializers import AppAPIsOrganisationModelListSerializer, APPAPIsCategoryModelListSerializer
from ..models import OrganisationDoctorModel,OrganisationModel, CategoryModel
from django_filters.rest_framework import DjangoFilterBackend

#--API for OrganisationDoctorModel to show a list of labs in homepage--#
class AppAPIsOrganisationModelDiagnosisListAPIView(generics.ListAPIView):
    queryset=OrganisationModel.objects.all()
    serializer_class=AppAPIsOrganisationModelListSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['org_type']
    # permission_classes = [permissions.IsAuthenticated]


class APPAPIsCategoryModelListAPIView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class= APPAPIsCategoryModelListSerializer

    

