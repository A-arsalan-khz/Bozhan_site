from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from user.models import UserPublicinformation
from .serializers import User_Serializer
class User_view(ModelViewSet):
    queryset = UserPublicinformation.objects.all()
    serializer_class = User_Serializer
