from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer

from Model.models import *


class UserSerializer(ModelSerializer):
    class Meta :
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
        ]

