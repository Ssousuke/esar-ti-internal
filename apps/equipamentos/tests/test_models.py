from django.test import TestCase
from apps.equipamentos.models import TypeEquipment, Equipments


class ModelTest(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    @staticmethod
    def test_create_type_equipment():
        return TypeEquipment.objects.create(
            type='Notebook'
        )

    def test_create_equipment(self):
        return Equipments.objects.create(
            name='Notebook Dell I5 Nº 01',
            type=self.test_create_type_equipment()
        )

    def test_type_equipment_return_str(self):
        type_str = self.test_create_type_equipment()
        return self.assertEqual(type_str.__str__(), 'Notebook')

    def test_equipment_return_str(self):
        equipment = self.test_create_equipment()
        return self.assertEqual(equipment.__str__(), 'Notebook Dell I5 Nº 01')
