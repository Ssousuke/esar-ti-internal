from django.db import models

from apps.equipamentos.models import Equipments


class Networks(models.Model):
    ipv4_or_ipv6 = models.GenericIPAddressField(unique=True)
    equipment = models.OneToOneField(Equipments, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.ipv4
