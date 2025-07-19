from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Product_view

router = DefaultRouter()
router.register(r'products', Product_view, basename='products')

urlpatterns = [
    path('',include(router.urls))
]
