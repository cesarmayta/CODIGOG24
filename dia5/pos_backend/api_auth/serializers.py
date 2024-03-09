from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer
)
from django.contrib.auth.models import User
from .models import Empleado

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(self,user):
        token = super().get_token(user)
        token['usu_nom'] = user.username
        token['usu_id'] = user.id
        
        return token

