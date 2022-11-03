from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class NewVisitorTest(LiveServerTestCase):
    '''тест нового посетителя'''

    def setUp(self):
        '''установка'''
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.browser.get(self.live_server_url)

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        '''подтверждение строки в таблице списка'''
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно открыть страницу и внести те продукты, которые съел сегодня и
        получить его позже'''
        # Открываем домашнюю страницу
        self.browser.get('http://localhost:8000')

        # В заголовке и шапке страницы указано, что здесь можно записать рацион за сегодня
        self.assertIn('Мой список блюд на сегодня', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Мой список блюд на сегодня', header_text)


        # Предлагается ввести элемент списка продуктов
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Внесите данные'
        )

        # Вводим в текстовом поле "Говядина 100 гр"
        inputbox.send_keys('Говядина 100 гр')

        # Когда нажимаем enter, страница обновляется, и теперь страница содержит
        # "1: Говядина 100 гр" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        self.check_for_row_in_list_table('1: Говядина 100 гр')
        # В текстовое поле можно ввести еще продукты
        # Вводим "Картофель 200 гр"
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Картофель 200 гр')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        # Страница снова обновляется и теперь показывает оба элемента списка
        self.check_for_row_in_list_table('1: Говядина 100 гр')
        self.check_for_row_in_list_table('2: Картофель 200 гр')

        # Проверяем, запомнил ли сайт список. Сайт должен сгенерировать для
        # отдельного пользователя уникальный URL-адрес - об этом выводится
        # небольшой текст с пояснениями
        self.fail('Закончить тест')

        # Посещаем этот адрес и проверяем наличие там списка


if __name__ == '__main__':
    unittest.main(warnings='ignore')
