from django.urls import path
from . import views

app_name = 'equipments'
urlpatterns = [
    path('', views.list_equipments, name='list'),
    path('criar/novo/', views.CreateEquipment.as_view(), name='create_equipment'),
    path('editar/<int:pk>/', views.EditEquipment.as_view(), name='edit_equipment'),
    path('deletar/<int:pk>/', views.delete_equipment, name='delete_equipment'),
]
