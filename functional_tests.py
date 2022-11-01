from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class VisitorTest(unittest.TestCase):
    '''тест посетителя'''

    def setUp(self):
        '''установка'''
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()

    def test_can_open_table(self):
        '''тест: можно найти продукт и посмотреть'''
        # Открываем домашнюю страницу
        self.browser.get('http://localhost:8000')

        # В заголовке и шапке страницы указано, что здесь предоставляется инфа о пит ценности пищи
        self.assertIn('Питательная ценность продуктов', self.browser.title)
        self.fail('Закончить тест')

        # Сразу предлагается выбрать из выпадающего списка категорию продукта
        # Поле находится под надписью "Выберите категорию продукта"
        # Наводим курсор на поле с продуктами и выпадает список категорий продуктов
        # Щелкаем на выбранную категорию и попадаем на страницу со списком продуктов выбранной категории


if __name__ == '__main__':
    unittest.main(warnings='ignore')
