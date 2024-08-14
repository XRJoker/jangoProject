from django import forms
from .models import Stores
from .models import Item, StoreItem

class StoreForms(forms.ModelForm):
    class Meta:
        model = Stores
        fields = ('name',)
#        widgets = {"name":forms.TextInput(attrs={"class":"frm"})}

class AddItemForms(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','description', 'price',)


class AddItemInStore(forms.ModelForm):
    class Meta:
        model = StoreItem
        fields = ('item','amount', 'store',)
        widgets = {"store":forms.HiddenInput()}
