from tkinter.ttk import Widget
from django import forms

class SignUpForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    first_name = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Last name'}))