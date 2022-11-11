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




class NewVisitorTest(FunctionalTest):
    '''тест нового посетителя'''

    def test_can_start_a_list_for_one_user(self):
        '''тест: можно начать список для одного пользователя'''
        # Открываем домашнюю страницу
        self.browser.get('http://localhost:8000')

        # В заголовке и шапке страницы указано, что здесь можно записать рацион за сегодня
        self.assertIn('My food-list tomorrow', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Your food_list', header_text)


        # Предлагается ввести элемент списка продуктов
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Внесите данные'
        )
    #
        # Вводим в текстовом поле "Говядина 100 гр"
        inputbox.send_keys('Говядина 100 гр')

        # Когда нажимаем enter, страница обновляется, и теперь страница содержит
        # "1: Говядина 100 гр" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)


        self.wait_for_row_in_list_table('1: Говядина 100 гр')
        # В текстовое поле можно ввести еще продукты
        # Вводим "Картофель 200 гр"
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Картофель 200 гр')
        inputbox.send_keys(Keys.ENTER)

        # Страница снова обновляется и теперь показывает оба элемента списка
        self.wait_for_row_in_list_table('1: Говядина 100 гр')
        self.wait_for_row_in_list_table('2: Картофель 200 гр')

        # Проверяем, запомнил ли сайт список. Сайт должен сгенерировать для
        # отдельного пользователя уникальный URL-адрес - об этом выводится
        # небольшой текст с пояснениями
        self.fail('Закончить тест')

        # Посещаем этот адрес и проверяем наличие там списка

    def test_multiple_users_can_start_lists_at_different_urls(self):
        '''тест: многочисленные пользователи могут начать списки по разным url'''
        # user_1 начинает новый список
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Курица 200 гр')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Курица 200 гр')

        # user_1 замечает, что его список имеет уникальный URL-адрес
        user_1_list_url = self.browser.current_url
        self.assertRegex(user_1_list_url, '/lists/.+')

        # user_2 приходит на сайт
        # Используем новый сеанс браузера, тем самым обеспечивая, чтобы никакая
        # информация от user_1 не прошла через данные cookie и пр
        self.browser.quit()
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # user_2 посещает домашнюю страницу. Нет никаких признаков списка user_1
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Говядина 100 гр', page_text)
        self.assertNotIn('Картофель 200 гр', page_text)
        self.assertNotIn('Курица 200 гр', page_text)

        # user_2 начинает новый список, вводя новый элемент
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Молоко 1 л')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Молоко 1 л')

        # user_2 получает уникальный URL-адрес
        user_2_list_url = self.browser.current_url
        self.assertRegex(user_2_list_url, '/lists/.+')
        self.assertNotEqual(user_1_list_url, user_2_list_url)

        # Нет ни намека на список user_1
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Говядина 100 гр', page_text)
        self.assertIn('Молоко 1 л', page_text)
