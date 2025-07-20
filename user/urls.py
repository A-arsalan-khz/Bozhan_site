from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user/',views.user, name='user'),
    path('user-table/', views.user_table, name='user-table'),
    path('catalog/', views.catalog,name='catalog'),
    path('guarantee/', views.guarantee,name='guarantee'),
    path('COC/', views.COC,name='COC'),
    path('after_sale_form/', views.after_sale_form,name='after_sale_form'),
    path('montage_form/', views.montage_form,name='montage_form'),
    path('material_quality_form/', views.material_quality_form,name='material_quality_form'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

