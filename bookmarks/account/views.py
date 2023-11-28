from django.http import  HttpResponse
from django.shortcuts  import render
from django.contrib.auth import  authenticate, login
from .forms import LoginForm,UserRegistrationForm,UserEditForm,ProfileEditForm
from django.contrib.auth.decorators import login_required
from . models import  Profile
from django.contrib  import  messages



def user_login(request):
    if request.method  == 'POST':
        form = LoginForm(request.POST)
        # The form is instantiated with the submitted data with form
        if form.is_valid():
            # The form is validated with form.is_valid(). If it is not valid, the form errors will be displayed
             # later in the template
            cd  = form.cleaned_data
            
            #If the submitted data is valid, the user gets authenticated against the database using the
            # authenticate() method
            """sumary_line
            
           This method takes the request object, the username, and the password
parameters and returns the User object if the user has been successfully authenticated, or
            """
            
            user = authenticate(request,username=cd['username'], password=cd['password'])
            
            
            
            if user  is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled  account')
            else:
                return HttpResponse('Invalid login')
    else:
        
        form  = LoginForm()
        return render(request, 'account/login.html',{'form':form})
            



#




#creating a view to  display a dashboard  when users log into their accounts
@login_required
#checks wether the current user is authenticated
def dashboard(request):
    return render(request, 'account/dashboard.html',{'section':'dashboard'})
# a dashboard view and a decorator  of django  authenticartion framework






#function that handles user registration
#view function is named register  and takes  a request object as a parameter
def register(request):
    # Check if the request method is 'POST', indicating that the user has submitted the form
    if request.method == 'POST':
        # If the request method is POST, create a 'UserRegistrationForm' instance with data from the POST request
        user_form = UserRegistrationForm(request.POST)
        
        # Check if the user_form is valid; if valid, proceed to create a new object without saving it immediately using commit=False
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            
            # The password for the new user is set using 'new_user.set_password()'; it is necessary when creating a new user in Django,
            # as it ensures the password is properly hashed
            new_user.save()
            
            
            #Creating the user  profile
            Profile.objects.create(user=new_user)
            #when users registered on site a Profile object will be created and associated 
            #with user object created
            
            # The new user object is then saved to the database using new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        # If the form is not valid, create a new instance of 'UserRegistrationForm'
        user_form = UserRegistrationForm()

    # Render the registration form template with the user_form as context
    return render(request,  'account/register.html', {'user_form': user_form})


#added  login_required decorator to view to allow authenticated users  be able to  edit their profiles
@login_required
def edit(request):
    if request.method  == 'POST':
        #if the requested method is post creates and instance of  from object UserEditForm and POST it
        
        user_form = UserEditForm(instance=request.user, data=request.POST)
        
              
#for this view we use two model forms UserEditForm to store the  data  of built-in User model
#and ProfileEditForm to store  additional personal data in custom Profile Model
        profile_form  = ProfileEditForm(
            instance = request.user.profile,
            data  = request.POST,
            files  = request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            #To validate data we u call is_valid() method  of both forms
            user_form.save()
            profile_form.save()
            #if both forms contain valid data  we both forms by  calling  save() method to update corresponding 
            #objects in database
            messages.success(request,'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
            #a success message is generated when users successfullyupdate their profile,if any of the forms contain
            #invalid data, an error is generated instead
    else:
         user_form  = UserEditForm(instance=request.user)
         profile_form  = ProfileEditForm(
             instance=request.user.profile) 
    return render(request, 'account/edit.html', {'user_form':user_form, 'profile_form':profile_form}) 
            
