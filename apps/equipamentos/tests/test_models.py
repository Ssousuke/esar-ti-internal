from django.test import TestCase
from apps.equipamentos.models import Equipments


class ModelTest(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    @staticmethod
    def test_create_equipment():
        return Equipments.objects.create(
            name='Notebook Dell I5 Nº 01',
            type='Notebook',
        )

    def test_equipment_return_str(self):
        equipment = self.test_create_equipment()
        return self.assertEqual(equipment.__str__(), 'Notebook Dell I5 Nº 01')
