from django import forms
from django.contrib.auth.models import  User

class LoginForm(forms.Form):
    username  = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    #This  form will be  used to authenticate  users  against the database  



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
    
    
#This fields will be validated according to  validations  of their corresponding  model fields
#example if a user picks  username that already exists , they will get a validation error  because 
#username  is a field  defined  with unique=True
def  clean_password2(self):
        cd  = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return  cd['password2']
""""


I haved added a  clean_password2 ()method to  compare  second password against first one
and raise an error  if the password  don't match
This method is executed when  form is validated by calling its  is_valid()method

""" 
           
              
      
      
      
      

      
        
    
    