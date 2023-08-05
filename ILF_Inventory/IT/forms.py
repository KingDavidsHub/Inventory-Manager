from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ITItem, ITStore
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class InventoryItemForm(forms.ModelForm):
    # project = forms.ModelChoiceField(queryset=Project.objects.all(),initial= 0 )
    class Meta:
        model = ITItem
        fields = ['staff_name', 'devices', 'model','floor', 'technical_description', 'computer_name', 'ser_no', 'win_version', 'supplier', 'date_purchased', 'warranty_period', 'warranty_expired', 'active', 'comment']



class InventoryStoreForm(forms.ModelForm):
    # project = forms.ModelChoiceField(queryset=Project.objects.all(),initial= 0 )
    class Meta:
        model = ITStore
        fields = ['name', 'total', 'amount_assigned','amount_left']


