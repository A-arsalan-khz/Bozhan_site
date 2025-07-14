from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username = request.data['username'])
    # password = get_object_or_404(User, password = request.data['password'])
    token,created = Token.objects.get_or_create(user = user)
    serializer = UserSerializer(user)
    if user.groups.filter(name = 'inspector').exists():
        redirect_url = '/inspector/'
    elif user.groups.filter(name = 'user').exists():
        redirect_url = '/user'
    else:
        return Response({"detail": "User group not recognized."}, status=status.HTTP_404_NOT_FOUND)
    return Response({
        "token": token.key,
        "user": serializer.data,
        "redirect_url": redirect_url
    })

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def test_token(request):
#     return Response("passed!".format(request.user.name))