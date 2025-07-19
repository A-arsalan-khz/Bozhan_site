from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def user(request):
    return render(request, "base/index3.html")

