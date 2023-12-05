from django.contrib import admin
from .models import Image
# Registering the image model in the administartion site





@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display  = ["title","slug","image","created"]
    list_filter = ['created']
    
