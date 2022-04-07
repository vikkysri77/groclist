from django import forms
from grocerieslist.models import OrderItem


class OrderItemForm(forms.ModelForm):
    item = forms.CharField()
    CHOICES = []
    client = forms.ChoiceField(label="Client Name", widget=forms.RadioSelect(choices=CHOICES))
    items_ordered = forms.CharField(label="Quantity")


class InterestForm(forms.Form):
    CHOICES = [(1, 'Yes'), (2, 'No')]
    interested = forms.RadioSelect(choices=CHOICES)
    quantity = forms.IntegerField(initial=1)
    comments = forms.CharField(label='Additional comments', required=False)
