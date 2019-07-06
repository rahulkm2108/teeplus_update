from django import forms

class Login(forms.Form):
   username = forms.CharField(max_length=30)
   password = forms.CharField(max_length=30)

class Registration(forms.Form):
    FirstName = forms.CharField(max_length=100)
    LastName = forms.CharField(max_length=100)
    Email = forms.EmailField()
    Number = forms.IntegerField()
    Password = forms.CharField(max_length=100)
    ConfirmPassword = forms.CharField(max_length=100)
