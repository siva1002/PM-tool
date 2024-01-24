from rest_framework import serializers
from .models import (User,Profile,Roles)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email',
                'username',
                'password',
                'age',
                'phone',
                'address',
                "role",
                'id',
                'role',
                "user_permissions",
                "groups"    
            ]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)  

class LoginViewSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

class UserUpdateSerializer(serializers.ModelSerializer):
    userrole=serializers.CharField(source='role.rolename',required=False)
    class Meta:
        model=User
        fields=['id','email','age','address','phone','username','role','userrole']
        read_only_fields = ('username','id')

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Roles
        fields="__all__"

