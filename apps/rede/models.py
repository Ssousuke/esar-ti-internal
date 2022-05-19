from django.db import models

from apps.equipamentos.models import Equipments


class Networks(models.Model):
    # departamento é um charfield
    department = models.CharField(max_length=100)
    # equipamento é um relacionamento 1 pra 1 com a tabela de equipamentos
    equipment = models.OneToOneField(Equipments, on_delete=models.SET_NULL, null=True, blank=True)
    # ipv4 ou ipv6
    ipv4_or_ipv6 = models.GenericIPAddressField(unique=True)

    def __str__(self):
        return self.ipv4_or_ipv6
