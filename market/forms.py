from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from market.models import Profile


class CreateMarketForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class MarketUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['market', 'address', 'phone', 'type']
