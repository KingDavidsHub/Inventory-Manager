from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import FacilityItem
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class InventoryItemForm(forms.ModelForm):
    # project = forms.ModelChoiceField(queryset=Project.objects.all(),initial= 0 )
    class Meta:
        model = FacilityItem
        fields = ['name', 'location', 'tag','owner', 'warranty_period', 'warranty_expired', 'active']


