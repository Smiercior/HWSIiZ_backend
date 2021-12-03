from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User
class CustomUserCreationForm(UserCreationForm):
    Abilities = forms.CharField(label='Abilities', min_length=4, max_length=64)
    BHPCourse = forms.BooleanField()
    class Meta:
        model = User
        fields = ('email','BHPCourse','Abilities')

class CustomUserChangeForm(UserChangeForm):
    Abilities = forms.CharField(label='Abilities', min_length=4, max_length=64)
    BHPCourse = forms.BooleanField()
    class Meta:
        model = User
        fields = ('email','username','password','BHPCourse','Abilities')
        #fields = UserChangeForm.Meta.fields