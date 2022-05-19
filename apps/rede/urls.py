from django.urls import path
from . import views

app_name = 'network'
urlpatterns = [
    path('', views.network_list, name='list'),
    path('criar/nova/rede/', views.CreateNetwork.as_view(), name='create_network'),
    path('editar/rede/<int:pk>/', views.UpdateNetNetwork.as_view(), name='edit_network'),
    path('deletar/rede/<int:pk>/', views.delete_network, name='delete_network'),
]
