from rest_framework import generics,status
from .serializers import AppAPIsOrganisationSlotBookingModelSlotListSerializer
from ..models import OrganisationSlotBookingModel
from organisation.models import OrganisationDoctorModel
from django_filters.rest_framework import DjangoFilterBackend


class AppAPIsOrganisationSlotBookingModelSlotListAPIView(generics.ListAPIView):
    serializer_class=AppAPIsOrganisationSlotBookingModelSlotListSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['date']

    def get_queryset(self):
        doc_id=self.kwargs['doc_id']
        instance= OrganisationDoctorModel.objects.get(id=doc_id)
        return instance.OrganisationSlotBookingModel_doctor.all()