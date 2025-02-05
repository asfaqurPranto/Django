from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('Add_recipe/', views.add_recipe, name='add_recipe'),
    path('search/', views.search, name='search'),
    path('delete/<str:recipe>/', views.Delete, name='Delete'),

    path('base/', views.view_base, name='base'),
]

