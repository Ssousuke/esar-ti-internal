from django.contrib import admin
from apps.rede.models import Department, Networks


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name'
    ]
    list_display_links = [
        'id',
        'name'
    ]


@admin.register(Networks)
class NetworkAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'department',
        'equipment',
        'ipv4_or_ipv6',
        'type'
    ]
    list_display_links = [
        'id',
        'department',
        'equipment',
        'ipv4_or_ipv6',
        'type'
    ]
