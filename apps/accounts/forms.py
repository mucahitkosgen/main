from django import forms

class sign_in(forms.Form):

    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget= forms.PasswordInput)
