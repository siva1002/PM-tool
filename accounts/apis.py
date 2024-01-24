from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated)
from .models import (Profile,User,Roles)
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
from rest_framework import generics
from accounts import serializer
from django.shortcuts import get_object_or_404
class UserCreateAPIView(generics.ListCreateAPIView):
    serializer_class=serializer.UserCreateSerializer
    queryset=User.objects.all()
    permission_classes=[AllowAny]
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return super().get_queryset()
        return super().get_queryset().filter(id=self.request.user.id)
    
    def list(self, request, *args, **kwargs):
        users=self.get_queryset()
        if not users:
            return Response(data=[],status=200)
        serialized=serializer.UserCreateSerializer(users,many=True)
        return Response(data=serialized.data,status=200)
    
    def post(self, request, *args, **kwargs):
        user = serializer.UserCreateSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        return Response(data={"errors":user.errors}, status=status.HTTP_206_PARTIAL_CONTENT)
    

class UserUpdateAPIview(generics.RetrieveUpdateAPIView):
    serializer_class=serializer.UserUpdateSerializer
    permission_classes=[IsAuthenticated]
    queryset=User.objects.all()
    def patch(self, request,pk, *args, **kwargs):
        user=get_object_or_404(User,pk=pk)
        updateuser=serializer.UserUpdateSerializer(user,data=request.data)
        if updateuser.is_valid():
            return Response(status=200,data=serializer.data)
        return Response(status=status.HTTP_206_PARTIAL_CONTENT,data={"error":updateuser.errors})
            
class ProfileCreateView(generics.ListCreateAPIView):
    serializer_class= serializer.ProfileSerializer
    queryset=Profile.objects.all()
    permission_classes=[IsAuthenticated]

    def list(self, request, *args, **kwargs):
        try:
            userprofile=Profile.objects.get(user=request.user)
            serialized=serializer.ProfileSerializer(userprofile)
            return Response(status=200,data=serialized.data)
        except:
            return Response(status=200,data={})

    def post(self, request, *args, **kwargs):
        profile=serializer.ProfileSerializer(data=request.data)
        if profile.is_valid():
            profile.save()
            return Response(status=200,data={"message":"Profile created successfully","data":profile.data})
        return Response(data={"errors":profile.errors}, status=status.HTTP_206_PARTIAL_CONTENT)
    
class ProfileUpdateDeleteAPIview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializer.ProfileSerializer
    queryset=Profile.objects.all()
    permission_classes=[IsAuthenticated]
    def patch(self, request,pk,*args, **kwargs):
            userprofile=get_object_or_404(Profile,pk=pk)
            updateprofile=serializer.ProfileSerializer(userprofile,data=request.data)
            if updateprofile.is_valid():
                updateprofile.save()
                return Response(status=200,data=serializer.data)
            return Response(status=status.HTTP_206_PARTIAL_CONTENT,data={"error":updateprofile.errors})

class LoginView(generics.CreateAPIView):

    serializer_class=serializer.LoginViewSerializer
    permission_classes=[AllowAny]
    queryset=User.objects.all()
    def post(self, request, *args, **kwargs):
        data=request.data
        username,password=data.get('username',None),data.get('password',None)
        user=authenticate(username=username,password=password)
        if user:
            token,created=Token.objects.get_or_create(user=user)
            data={"token":str(token),
                  "user":user.username}
            login(request, user=user)
            return Response(status=200,data={"message":"User Logged in successfully.","data":data})
        return Response(status=status.HTTP_404_NOT_FOUND,data={"message":"User Does Not Exist"})
        

class RoleCreateAPIView(generics.ListCreateAPIView):
    serializer_class=serializer.RolesSerializer
    queryset=Roles.objects.all()
    permission_classes=[IsAuthenticated]
    def list(self, request, *args, **kwargs):
        roles=Roles.objects.all()
        serialized=serializer.RolesSerializer(roles,many=True)
        return Response(status=status.HTTP_200_OK,data={"data":serialized.data})
    def create(self, request, *args, **kwargs):
        role=serializer.RolesSerializer(data=request.data)
        if role.is_valid():
            role.save()
            return Response(status=200,data={"message":"Role created successfully","data":role.data})
        return Response(data={"errors":role.errors}, status=status.HTTP_206_PARTIAL_CONTENT)


class RoleUpdateAPIview(generics.RetrieveUpdateAPIView):
    serializer_class=serializer.RolesSerializer
    permission_classes=[IsAuthenticated]
    queryset=Roles.objects.all()
    def patch(self, request,pk, *args, **kwargs):
        role=get_object_or_404(Roles,pk=pk)
        updaterole=serializer.RolesSerializer(role,data=request.data)
        if updaterole.is_valid():
            return Response(status=200,data=updaterole.data)
        return Response(status=status.HTTP_206_PARTIAL_CONTENT,data={"error":updaterole.errors})