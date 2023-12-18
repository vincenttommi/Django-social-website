from django.db import  models
from django.conf import  settings
from django.utils.text import slugify



#This model will be used to store  images in the platform
class  Image(models.Model):
    user  = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='images_created',on_delete=models.CASCADE)
    #The user that bookmarked the image
    title  = models.CharField(max_length=200)
    #title for the image
    slug  =  models.SlugField(max_length=200, blank=True)
    #A short label that contains only letters, numbers , underscores, or hyphens to be used for 
    #building beautiful SEO-freindly URLs
    url =  models.URLField(max_length=2000)
    image =  models.ImageField(upload_to='images/%Y/%m/%d/')
    #field for capturing image file
    description  = models.TextField(blank=True)
    #field for handling description
    created  = models.DateField(auto_now_add=True)
    #The date and time  that indicate when the object  was created in database
    users_like  = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='images_liked',blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug  = slugify(self.title)
        super().save(*args, **kwargs)       
        #when the aa Image  object is saved , if the  slug field doesn't have 
        # a value , the slugify() is used  to automatically  generate  a slug from the title field
        #of the image
            
    
    
    class  Meta:
        
        indexes = [
            
            models.Index(fields=['-created']),
    
        ]
        ordering  = ['-created']
        
        
        def __str__(self):
            return self.title
        
    