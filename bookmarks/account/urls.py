from django.urls import  path
from . import views
from django.contrib.auth import views as  auth_views



urlpatterns = [
    
    # path('login/', views.user_login, name='login')
    #logout and login views
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name ='logout'),
    #registering dashboard view
    path('', views.dashboard, name='dashboard'),
    #view for changing password
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    #will handle  the form to change  the password
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view() ,name='password_change_done'),
    #will display  a succes message  after the  user has  successfully  changed  their password

    #Reset password urls
    path('password-reset/',auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/'),
    
    
]



