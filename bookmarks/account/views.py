from django.http import  HttpResponse
from django.shortcuts  import render
from django.contrib.auth import  authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required




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