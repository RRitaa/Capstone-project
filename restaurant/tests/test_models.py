from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title= "Lemon Dessert", price= 10, inventory= 1)
        itemstr = item.get_item()
        
        self.assertEqual(itemstr, "Lemon Dessert : 10")