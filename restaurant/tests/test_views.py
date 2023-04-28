from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self) ->None:
        self.client = Client()
        self.user = User.objects.create_user(
            username='testusert',            
            password='lemon@799!'
        )
        self.LemonDessert = Menu.objects.create(title='Lemon Dessert', price = 10, inventory = 1 )
        self.Bruschetta = Menu.objects.create(title='Bruschetta', price= 11, inventory =1)
        
    def loginAsTestUser(self) ->None:
        self.client.login(username='testuser', password='lemon@799!')
        
    def test_view_authentication(self) -> None:
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        self.loginAsTestUser()
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_getall(self):
        self.logInAsTestUser()
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)
    