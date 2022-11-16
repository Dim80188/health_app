from django.test import TestCase
from food.forms import ItemForm
from food.forms import EMPTY_ITEM_ERROR, ItemForm

class ItemFormTest(TestCase):
    '''тест формы для элемента списка'''

    def test_form_renders_item_text_input(self):
        '''тест: форма отображает текстовое поле ввода'''
        form = ItemForm()

        # self.fail(form.as_p())

    def test_form_item_input_has_placeholder_and_css_classes(self):
        '''тест: поле ввода имеет атрибут placeholder и css-классы'''
        form = ItemForm()
        self.assertIn('placeholder="Enter data"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        '''тест валидации формы для пустых элементов'''
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'],
            [EMPTY_ITEM_ERROR]
        )