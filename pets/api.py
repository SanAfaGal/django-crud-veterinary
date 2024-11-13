from rest_framework import viewsets, permissions

from .models import Customer, Pet
from .serializers import CustomerSerializer, PetSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PetSerializer
