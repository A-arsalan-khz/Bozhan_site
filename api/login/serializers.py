from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(many=True)
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password','groups']
