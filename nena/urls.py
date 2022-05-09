from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamentos/', include('apps.equipamentos.urls', namespace='equipments')),
    path('rede/', include('apps.rede.urls', namespace='network')),
]
