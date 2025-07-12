from django.urls import path,include

urlpatterns = [
    path('', include('api.login.urls')),
    # path('inspector/', include('api.inspector.urls')),
    # path('user/', include('api.user.urls'))
]
