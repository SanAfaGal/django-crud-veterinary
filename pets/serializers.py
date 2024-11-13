from rest_framework import serializers

from .models import Customer, Pet


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = 'id_customer',  # Comma (,) at the end 'cause it's a tuple


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
        read_only_fields = 'id_pet',  # Comma (,) at the end 'cause it's a tuple
