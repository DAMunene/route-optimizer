from rest_framework import serializers
from .models import FuelPrice

class FuelStopSerializer(serializers.ModelSerializer):
    distance = serializers.FloatField()
    
    class Meta:
        model = FuelPrice
        fields = ['truckstop_name', 'address', 'city', 'state', 'retail_price', 'distance']