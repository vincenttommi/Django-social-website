from django.db import models
from  django.conf  import settings


class  Profile(models.Model):
    user  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
    date_of_birth = models.DateField(blank=True, null=True)
    photo  = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    #We have made this field  optional with blank=True and an ImageField that manages the storage 
    #of image files
    
    
    
    
def  __str__(self):
    return  f'Profile of {self.user.username}'
    
#Employs one to one field where a user will be  used to associate profile with users.
 
    