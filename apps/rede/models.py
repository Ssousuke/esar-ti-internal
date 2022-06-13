from django.db import models

TYPE_EQUIPMENT_CHOICES = (
    ('Notebook', 'Notebook'),
    ('Computador', 'Computador'),
    ('Impressora', 'Impressora'),
    ('Roteador', 'Roteador'),
    ('Outros', 'Outros'),
)


class Department(models.Model):
    name = models.CharField(max_length=80, verbose_name='Setor')

    def __str__(self):
        return self.name


class Networks(models.Model):
    # departamento é um charfield
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Setor')

    # equipamento é uma charfield unico
    equipment = models.CharField(max_length=100, null=True, blank=True, unique=True, verbose_name='Equipamento')
    # ipv4 ou ipv6
    ipv4_or_ipv6 = models.GenericIPAddressField(unique=True, verbose_name='IPv4 / IPv6')

    # tipo de equipamento
    type = models.CharField(max_length=10, choices=TYPE_EQUIPMENT_CHOICES, verbose_name='Tipo', null=True, blank=True)

    def __str__(self):
        return self.ipv4_or_ipv6

    class Meta:
        ordering = ['-ipv4_or_ipv6']
