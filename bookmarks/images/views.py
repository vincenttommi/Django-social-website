from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from.forms import ImageCreateForm






@login_required
def image_create(request):
    # Check if the request method is 'POST'
    if request.method == 'POST':
        # Initialize the form with data from the POST request
        form = ImageCreateForm(data=request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Extract cleaned data from the form
            cd = form.cleaned_data

            # Create a new image instance, but don't save it to the database yet
            new_image = form.save(commit=False)

            # Assign the current user to the image instance
            new_image.user = request.user

            # Save the image object to the database
            new_image.save()

            # Display a success message using Django messaging framework
            messages.success(request, 'Image added successfully')

            # Redirect the user to the canonical URL of the new image
            return redirect(new_image.get_absolute_url())
    else:
        # Build the form with data provided by the bookmark via GET
        form = ImageCreateForm(data=request.GET)

    # Return a render response for 'GET' requests
    return render(request, 'image/create.html', {'section': 'images', 'form': form})
