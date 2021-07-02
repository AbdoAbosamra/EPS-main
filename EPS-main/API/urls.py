from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    ################ User ########################
    path('User/' , UserListAPIVeiw.as_view() ) ,
    path('User/create' , UserCreateAPIVeiw.as_view() ) ,
    path('User/<pk>' , UserRetieveAPIVeiw.as_view() ) ,
    path('User/<pk>/edit' , UserUpdateListAPIVeiw.as_view() ) ,
    path('User/<pk>/delete' , UserDestroyAPIView.as_view() ) ,
    path('', frist_page, name='frist_page'),
    path('user_home/', User_Home, name='user_home'),
    path('admin_home/', Admin_Home, name='admin_Home'),
    path('login/', loginpage, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout1, name='logout'),
    path('form/', Form, name='Form'),
]