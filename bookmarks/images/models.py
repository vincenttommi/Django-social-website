from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    # This captures the user that bookmarked the images and employs a foreign key 
    # that shows a one-to-many relationship because images are posted by one user.
    
    title = models.CharField(max_length=200)
    # Title of the image.

    slug = models.SlugField(max_length=200, blank=True)
    # A short label that contains only letters, numbers, underscores, or hyphens 
    # to be used for building beautiful SEO-friendly URLs.
      
    url = models.SlugField(max_length=2000) 
      
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    # The image file.

    description = models.TextField(blank=True)
    # An optional description for the image.

    created = models.DateField(auto_now_add=True)
    # The date and time that indicate when the object was created in the database.

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)
    # A field that stores the users who like an image and employs a many-to-many relationship 
    # because a user might like multiple images and each image can be liked by multiple users.

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        # When an Image is saved, if the slug field doesn't have a value, 
        # the slugify() function is used to automatically generate a slug 
        # from the title field of the image.
