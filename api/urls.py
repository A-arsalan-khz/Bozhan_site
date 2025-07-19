from django.urls import path,include

urlpatterns = [
    path('', include('api.login.urls')),
    path('',include('api.inspector.urls')),
    path('',include('api.user.urls'))
    # path('inspector/', include('api.inspector.urls')),
    # path('user/', include('api.user.urls'))
]
