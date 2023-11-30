from django.contrib import  admin
from django.urls import path,include
from django.conf import  settings
from django.conf.urls.static import  static



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('social-auth/', include('social_django.urls', namespace='social'))
    #adding social authentication to the projects that allows users to authenticate with
    #Facebook,Twitter and Google backends
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#We have added the static() helper function to serve files with Django development server during 
#development

#N/B The static helper function is suitable  for development but not  production use.
 
    