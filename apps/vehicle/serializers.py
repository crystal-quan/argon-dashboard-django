# vehicle/serializers.py
from rest_framework import serializers
from .models import Vehicle, VehicleCategory


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'is_active', 'created_by', 'created_at', 'updated_at', 'deleted_at']


class VehicleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCategory
        fields = ['id', 'name', 'description', 'vehicle_type', 'is_active', 'created_by', 'created_at', 'updated_at',
                  'deleted_at']
