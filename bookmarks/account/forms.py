from django import forms

class LoginForm(forms.Form):
    username  = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    #This  form will be  used to authenticate  users  against the database  