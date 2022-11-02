from django.test import TestCase
from django.urls import resolve
from .views import home_page
from django.http import HttpRequest

# Create your tests here.

class HomePageTest(TestCase):
    '''тест домашней страницы'''



    def test_uses_home_template(self):
        '''тест: используется домашний шаблон'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
