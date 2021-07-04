from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import (
    ListAPIView ,
    RetrieveAPIView ,
    UpdateAPIView ,
    DestroyAPIView ,
    CreateAPIView ,
)
from django.core import serializers

from Model.models import *
from .permisions import InOwnerOrReadOnly

from .serializers import *

from rest_framework.permissions import (
    AllowAny ,
    IsAuthenticated ,
    IsAdminUser ,
    IsAuthenticatedOrReadOnly
)
import json


########### User ###############

class UserListAPIVeiw(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserCreateAPIVeiw(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes = [IsAuthenticated , IsAdminUser]
    def preform_create(self , serializer):
        serializer.save(user = self.request.user)

class UserUpdateListAPIVeiw(UpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserRetieveAPIVeiw(RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from django.shortcuts import render
from django.contrib import auth
from numpy.core.fromnumeric import cumprod
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Model.form import *
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import *
from Model.decorators import unauthenticated_user, allowed_users, admin_only
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import svm
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def User_Home(request):
    pk = request.user.id
    quiz_veiw(request)
    student = Student.objects.get(user=pk)
    data = serializers.serialize('json', [student, ])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data, content_type="application/json")











