"""
URL configuration for project21 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from profile_part.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name="login"),
    path('register/', register_page,name="base"),

    path('home/', home, name="home"),
    path('edit_profile/', edit_profile,name="edit_profile"),
    path('viewprofile/',view_profile,name="view_profile"),
    path('update_profile/',update_profile,name="update_profile"),

    path('subcatagory/<str:name>/',subcatagory,name="subcatagory"),
    path('people/<str:profession>/',search_by_profession,name="professions"),
    path('search_profiles/',search_by_profession,name="professions"),
    path('search_result/',search_result,name="search_result"),
    path('userdetails/<str:email>/',userdetails, name="userdetails"),

    path('filterresult/',filterresult,name="filterresult"),
    path('meeting/',videocall,name="meeting"),


    # path('logout/', logout_page, name='logout'),

    # path('',base,name="base")
]
