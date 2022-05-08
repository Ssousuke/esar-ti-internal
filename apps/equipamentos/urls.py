from django.urls import path
from . import views

app_name = 'equipments'
urlpatterns = [
    path('lista/', views.list_equipments, name='list'),
]
