from django.db import models


class TypeEquipment(models.Model):
    type = models.CharField(max_length=80)

    def __str__(self):
        return self.type


class Equipments(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(TypeEquipment, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    maintenance = models.BooleanField(default=False)

    def __str__(self):
        return self.name
