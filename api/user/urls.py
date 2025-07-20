from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import User_view,UserFormaftersale_view,UserFormpartssystemsqualityrating_view,UserFormvehicleassemblyquality_view

router = DefaultRouter()
router.register(r'user', User_view, basename='user')
router.register(r'userform1', UserFormaftersale_view, basename='userform1')#UserFormaftersale_view
router.register(r'userform2', UserFormpartssystemsqualityrating_view, basename='userform2')#UserFormaftersale_view
router.register(r'userform3', UserFormvehicleassemblyquality_view, basename='userform3')

urlpatterns = [
    path('',include(router.urls))
]
