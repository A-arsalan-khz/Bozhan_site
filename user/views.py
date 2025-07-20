from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from .models import UserFormaftersale,UserFormpartssystemsqualityrating
# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def user(request):
    return render(request, "base/index3.html")
def user_table(request):
    return render(request, "base/user_table.html")
def catalog(request):
    return render(request, "base/catalog.html")
def guarantee(request):
    return render(request, "base/guarantee.html")
def COC(request):
    return render(request, "base/COC.html")
def after_sale_form(request):
    data = UserFormaftersale.objects.all()  # Fetch all records
    return render(request, 'base/after_sale_form.html', {'data': data})
def montage_form(request):
    data = UserFormpartssystemsqualityrating.objects.all()
    return render(request, "base/montage_form.html",{"data":data})
def material_quality_form(request):
    return render(request, "base/material_quality_form.html")

