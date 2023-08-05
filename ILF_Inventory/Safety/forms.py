from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import SafetyItem, SafetyStore
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = SafetyItem
        fields = ['staff_name','item_name' ,'quantity', 'floor', 'project']



class InventoryStoreForm(forms.ModelForm):
    class Meta:
        model = SafetyStore
        fields = ['name','total' ,'assigned', 'left']