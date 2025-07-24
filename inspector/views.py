from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def inspector(request):
    return render(request, "base/index.html")

def Exclusive_Manufacturer_System(request):
    vin = request.GET.get('vin')  
    return render(request, 'base/Exclusive_Manufacturer_System.html', {'vin': vin})

def COP(request):
    return render(request, 'base/COP.html')

def date(request):
    return render(request,'base/dates.html')