from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        label='Rol'
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'grupo') 