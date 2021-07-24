from django import forms
from django.forms import fields
from .models import Item, Combination, User
from django.contrib.auth.forms import UserCreationForm

class CombinationForm(forms.ModelForm):
    class Meta:
        model = Combination
        fields = ['name', 'Item']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['brand', 'category', 'color_main', 'color_sub', 'size', 'user', 'tags', 'image']

