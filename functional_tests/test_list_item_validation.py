from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from unittest import skip
import time
from .base import FunctionalTest




class ItemValidationTest(FunctionalTest):
    '''тест валидации элемента списка'''
    
    def test_cannot_add_empty_list_items(self):
        '''тест: нельзя добавлять пустые элементы списка'''
        # Пользователь открывает домашнюю страницу и случайно пытается отправить
        # пустой элемент списка. Он нажимает Enter на пустом поле ввода
        #
        # Домашняя страница обновляется, и появляется сообщение об ошибке,
        # которое говорит, что элементы списка не должны быть пустыми
        #
        # Он пробует снова, теперь с неким текстом для элемента, и теперь это срабатывает
        #
        # Как ни странно, пользователь решает отправить второй пустой элемент списка
        #
        # Он получает аналогичное предупреждение на странице списка
        #
        # И он может его исправить, заполнив поле неким текстом
