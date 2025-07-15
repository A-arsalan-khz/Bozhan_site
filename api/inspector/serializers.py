from rest_framework import serializers
from inspector.models import Products

class Products_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id','variant','vin']