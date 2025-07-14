from django.urls import path, include
from .views import ListUsers
urlpatterns = [
    path('inspector/', ListUsers.as_view(), name='inspector')
]
