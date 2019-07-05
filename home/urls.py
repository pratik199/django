from django.urls import path
from .views import *

urlpatterns = [
    #path('',homee,name='home'),
    path('',homee),
    path('about',about),
    path('contact',contact),
    path('boot',boot),
    path('homee',homee),
    path('delete-student/<id>',deletestudent),
    path('edit-student/<id>',editstudent),
    path('create-student',createstudent),

    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('register/',register,name='register'),
    
    
    
]