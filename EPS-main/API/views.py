from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import (
    ListAPIView ,
    RetrieveAPIView ,
    UpdateAPIView ,
    DestroyAPIView ,
    CreateAPIView ,
)
from Model.models import *
from .permisions import InOwnerOrReadOnly

from .serializers import *

from rest_framework.permissions import (
    AllowAny ,
    IsAuthenticated ,
    IsAdminUser ,
    IsAuthenticatedOrReadOnly
)

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
