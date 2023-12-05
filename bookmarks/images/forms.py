from django  import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model  = Image
        fields  = ['title','url','description']
        widgets  = {
            'url': forms.HiddenInput,
        }
    #defined a model form from Image model, including only the title,url,and description fields 
    #users will not enter  the image URL directly in the form
    def  clean_url(self):
        
        url = self.cleaned_data['url']
        valid_extensions  = ['jpg','jpeg','png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid  image extension')
        
        return url
    #defined a value  url field  to retieve the method  to clean url field
    # The value  of url is retrieved  by accessing the cleaned_data dictionary of the form instance
    
   #URL is split to check wether  the file has a valid extension , if the  ValidationError is raised 
   #the  form instance  is not validated
    
   