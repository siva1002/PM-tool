from rest_framework import serializers
from .models import (User,Profile)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','username','password','age','phone','address']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)  

class LoginViewSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()