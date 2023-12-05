from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from.forms import ImageCreateForm




#a view to  store images  on the site
@login_required
#login_required decorator to image_create view to prevent access to unauthenticated users
def  image_create(request):
    if request.method  == 'POST':
        #initial data  has to be  provided throught HTTP request inorder to create an instance
        #of the form,data will consist of url and title attributes of image from external source
        form  = ImageCreateForm(data=request.POST)
        
        #when form is submitted  with POST HTTP request, its validated  with form.is_valid()
        #if the form is valid , a new image instance is created by saving form with form
        if form.is_valid():
            #form data is valid
            cd = form.cleaned_data
            new_image  = form.save(commit=False)
            #assign current user to the item
            new_image.user  = request.user
            #a new relationship to current user performing the request is added to new Image Instance
            #with new_image.user  = request.user
            #This is how we will know who uploaded each image
            new_image.save()
            #saving image object to the database
            messages.success(request,'Image added successfully')
            #a success message is created using Django messaging framework   and user
            #is redirected  to canonical URL of the new image
            return redirect(new_image.get_absolute_url())
    else:
        #build  form with data provided by the  bookmark via GET
        
        form  = ImageCreateForm(data=request.GET)
        
        return render(request, 'images/image/create.html', {'section':'images', 'form':form})