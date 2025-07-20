from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from user.models import UserPublicinformation,UserFormaftersale,UserFormpartssystemsqualityrating,UserFormvehicleassemblyquality
from .serializers import User_Serializer,UserFormaftersale_Serializer,UserFormpartssystemsqualityrating_Serializer,UserFormvehicleassemblyquality_Serializer
class User_view(ModelViewSet):
    queryset = UserPublicinformation.objects.all()
    serializer_class = User_Serializer



class UserFormaftersale_view(ModelViewSet):
    queryset = UserFormaftersale.objects.all()
    serializer_class = UserFormaftersale_Serializer



class UserFormpartssystemsqualityrating_view(ModelViewSet):
    queryset = UserFormpartssystemsqualityrating.objects.all()
    serializer_class = UserFormpartssystemsqualityrating_Serializer



class UserFormvehicleassemblyquality_view(ModelViewSet):
    queryset = UserFormvehicleassemblyquality.objects.all()
    serializer_class = UserFormvehicleassemblyquality_Serializer
