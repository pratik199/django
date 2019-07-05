"""djproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    #path('',views.home_view),
    path('',views.homee),
    path('homee/',include('home.urls')),
    # path('about',views.about),
    # path('contact',views.contact),
    # path('boot',views.boot),
    # path('homee',views.homee),
    # path('delete-student/<id>',views.deletestudent),
    # path('edit-student/<id>',views.editstudent),
    # path('create-student',views.createstudent),
     path('admin/', admin.site.urls),
    
    
]
