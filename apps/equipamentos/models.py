from django.db import models


class Equipments(models.Model):
    TYPE_EQUIPMENT_CHOICES = (
        ('Notebook', 'Notebook'),
        ('Computador', 'Computador'),
        ('Impressora', 'Impressora'),
        ('Roteador', 'Roteador'),
        ('Outros', 'Outros'),
    )

    name = models.CharField(max_length=255, verbose_name='Nome')
    type = models.CharField(max_length=10, choices=TYPE_EQUIPMENT_CHOICES, verbose_name='Tipo')
    status = models.BooleanField(default=True, verbose_name='Disponível')

    def __str__(self):
        return self.name
