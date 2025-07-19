from rest_framework import serializers
from user.models import UserPublicinformation

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserPublicinformation
        fields = ['id','type_approval_number','typee','brand_name','category','model','color',
                'production_date', 'delivery_date', 'vin', 'essential_accessories', 'additional_features',
                'net_power_of_motive_forces', 'torque', 'maximum_speed', 'fuel_consumption', 'energy_rating',
                'battery_type', 'battery_capacity', 'navigation_per_charge', 'pure_mass', 'maximum_permissible_technical_mass',
                'pollution_standard_level', 'static_sound_level', 'guarantee_period'
                 ]