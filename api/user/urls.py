from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import User_view

router = DefaultRouter()
router.register(r'user', User_view, basename='user')

urlpatterns = [
    path('',include(router.urls))
]
