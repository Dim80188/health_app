from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class VisitorTest(unittest.TestCase):
    '''тест посетителя'''

    def setUp(self):
        '''установка'''
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()

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
            'Enter item'
        )

        # Вводим в текстовом поле "Говядина 100 гр"
        inputbox.send_keys('Говядина 100 гр')

        # Когда нажимаем enter, страница обновляется, и теперь страница содержит
        # "1: Говядина 100 гр" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(BY.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Говядина 100 гр' for row in rows)
        )
        # В текстовое поле можно ввести еще продукты
        # Вводим "Картофель 200 гр"
        # Страница снова обновляется и теперь показывает оба элемента списка
        self.fail('Закончить тест')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
