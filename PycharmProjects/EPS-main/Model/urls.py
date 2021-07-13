from django.contrib import admin
from django.urls import path , include ,re_path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('' , frist_page , name='frist_page'),

    #path('user_home/quizelist',quiz_veiw , name='quiz_veiw'),
    #path('admin_home/', Admin_Home, name='admin_Home'),

################### Admin ##############################
    path('Admin/', include("Model.urls2")),

#########################  User Page  #######################
    path('user_home/', User_Home, name='user_home'),
    path('logout/', logout1, name='logout'),
    path('form/',Form,name='Form'),

    ################### Quiz ##############################

    path('list/' ,quiz_veiw , name='quiz_veiw'),
    path('list/<pk>/' ,quizpk_veiw , name='quizpk_veiw'),
    path('list/<pk>/sava/' ,save_quiz_view , name='save_view'),
    path('list/<pk>/data' ,quiz_data_view , name='quiz_data_view'),



]


