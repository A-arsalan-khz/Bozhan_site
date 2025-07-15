from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from inspector.models import Products
from .serializers import Products_Serializer
class Product_view(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = Products_Serializer
    lookup_field = 'vin'