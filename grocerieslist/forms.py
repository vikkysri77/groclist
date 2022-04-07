from django import forms
from .models import OrderItem
from django.forms import RadioSelect, TextInput

class OrderItemForm(forms.ModelForm):
    class Meta:
        model=OrderItem
        fields = ['item', 'client', 'itemsCount']
        widgets = {
        'client': RadioSelect(),
        'itemsCount': TextInput(),
        }
        labels = {
        'client': 'Client Name',
        'itemsCount': 'Quantity'
        }

class InterestForm(forms.Form):
    CHOICES = [(1, 'Yes'), (2, 'No')]
    interested = forms.RadioSelect(choices=CHOICES)
    quantity = forms.IntegerField(initial=1)
    comments = forms.CharField(label='Additional comments', required=False)



