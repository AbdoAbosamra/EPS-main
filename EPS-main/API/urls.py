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
    path('user_home/', User_Home, name='user_home_api'),

]