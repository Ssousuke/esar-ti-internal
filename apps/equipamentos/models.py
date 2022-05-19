from django.db import models


class Equipments(models.Model):
    # tipos de equipamentos disponíveis
    TYPE_EQUIPMENT_CHOICES = (
        ('Notebook', 'Notebook'),
        ('Computador', 'Computador'),
        ('Impressora', 'Impressora'),
        ('Roteador', 'Roteador'),
        ('Outros', 'Outros'),
    )
    # nome do equipamento
    name = models.CharField(max_length=255, verbose_name='Nome')
    # tipo do equipamento
    type = models.CharField(max_length=10, choices=TYPE_EQUIPMENT_CHOICES, verbose_name='Tipo')
    # status do equipamento
    status = models.BooleanField(default=True, verbose_name='Disponível')

    #  quando isntanciada o objeto criado é chamado pelo atributo nome
    def __str__(self):
        return self.name
