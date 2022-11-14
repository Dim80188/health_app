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
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        #
        # Домашняя страница обновляется, и появляется сообщение об ошибке,
        # которое говорит, что элементы списка не должны быть пустыми
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "You can't have an empty list item"
        ))
        #
        # Он пробует снова, теперь с неким текстом для элемента, и теперь это срабатывает
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Buy milk')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        #

        # Как ни странно, пользователь решает отправить второй пустой элемент списка
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)

        #
        # Он получает аналогичное предупреждение на странице списка
        self.wait_for(lambda: self.assertEqual(
        self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
        "You can't have an empty list item"
        ))
        #
        # И он может его исправить, заполнив поле неким текстом
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Make tea')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
