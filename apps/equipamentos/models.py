from django.db import models


class TypeEquipment(models.Model):
    type = models.CharField(max_length=80)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'


class Equipments(models.Model):
    name = models.CharField(max_length=255)
    # ipv4
    type = models.ForeignKey(TypeEquipment, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    maintenance = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
