from django.urls import path, re_path
from . import views

urlpatterns = [

    # The home page
    path('', views.index, name='admin_Home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='admin_pages'),

]