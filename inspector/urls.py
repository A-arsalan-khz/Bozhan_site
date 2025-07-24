from django.urls import path, include
from . import views

urlpatterns = [
    path('products/',views.inspector, name='products'),
    path('Exclusive_Manufacturer_System/',views.Exclusive_Manufacturer_System, name = 'Exclusive_Manufacturer_System'),
    path('Exclusive_Manufacturer_System/COP/',views.COP,name='COP'),
    path("Exclusive_Manufacturer_System/date/",views.date, name="date")
]

