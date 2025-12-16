from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import User


# creating a registration form
class UserRegistrationForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    
    
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']