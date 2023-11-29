from django.contrib.auth.models import  User



class EmailAuthBackend:
    "Authenticate using an e-mail address"

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            # The user with given email address is retrieved and he passowrd is checked 
            #using built-in check_password() method of the user model
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None
        #This method handles password hashing to compare  given password stored in database
# The preceding code is  a simple authentication backend. authenticate()  method recieves  a request object
# and username and password as optional parameteres 


def  get_user(self, user_id):
    try:
         return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return None
    
#getting a user through the ID provided in the user_id parameter 
                
    