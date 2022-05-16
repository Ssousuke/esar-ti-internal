from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamentos/', include('apps.equipamentos.urls', namespace='equipments')),
    path('rede/', include('apps.rede.urls', namespace='network')),
    path('', include('apps.accounts.urls', namespace='accounts')),
    path('dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
]
