from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import BusinessItem, BusinessStore
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = BusinessItem
        fields = ['staff_name','item_name' ,'quantity', 'floor']



class InventoryStoreForm(forms.ModelForm):
    class Meta:
        model = BusinessStore
        fields = ['name','total' ,'assigned', 'left']