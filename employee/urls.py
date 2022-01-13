from django.contrib import admin
from django.urls import path 
from .import views



urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginpage,name='loginpage'),
    path('register/',views.registerpage,name='registerpage'),
    path('employeee_list/',views.list_emp,name='list_emp'),
    path('delete/<str:pk>/',views.Delete,name='delete'),
    path('update/<str:pk>/',views.Update,name='update'),
    path('logout/',views.logoutPage, name='logout'),
]