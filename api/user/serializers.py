from rest_framework import serializers
from user.models import UserPublicinformation
from user.models import UserFormaftersale
from user.models import UserFormpartssystemsqualityrating
from user.models import UserFormvehicleassemblyquality

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserPublicinformation
        fields = ['type_approval_number','typee','brand_name','category','model','color',
                'production_date', 'delivery_date', 'vin','engine_number', 'essential_accessories', 'additional_features',
                'pure_mass', 'maximum_permissible_technical_mass',
                'pollution_standard_level', 'static_sound_level', 'guarantee_period'
                ]


class UserFormaftersale_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserFormaftersale
        fields = '__all__'


class UserFormpartssystemsqualityrating_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserFormpartssystemsqualityrating
        fields = '__all__'


class UserFormvehicleassemblyquality_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserFormvehicleassemblyquality
        fields = '__all__'