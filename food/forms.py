from django import forms
from food.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"

class ItemForm(forms.models.ModelForm):
    '''форма для элементов списка'''

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
            'placeholder': 'Enter data',
            'class': 'form-control input-lg',
        })
        }
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }