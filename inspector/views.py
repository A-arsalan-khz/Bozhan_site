from django.shortcuts import render
from django.http import HttpResponse
def inspector(request):
    return HttpResponse("hello")