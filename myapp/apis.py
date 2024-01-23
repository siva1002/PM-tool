from rest_framework.generics import (ListCreateAPIView,
                                     CreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from .serializer import (ProfileSerializer,
                         UserCreateSerializer,
                         LoginViewSerializer)
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated)
from .models import (Profile,User)
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token

class UserCreateAPIView(ListCreateAPIView):
    serializer_class=UserCreateSerializer
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
        serialized=UserCreateSerializer(users,many=True)
        return Response(data=serialized.data,status=200)
    
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ProfileCreateView(ListCreateAPIView):
    serializer_class= ProfileSerializer
    queryset=Profile.objects.all()
    permission_classes=[IsAuthenticated]

    def list(self, request, *args, **kwargs):
        try:
            userprofile=Profile.objects.get(user=request.user)
            serialized=ProfileSerializer(userprofile)
            return Response(status=200,data=serialized.data)
        except:
            return Response(status=200,data={})

    def post(self, request, *args, **kwargs):
        profile=ProfileSerializer(data=request.data)
        if profile.is_valid():
            profile.save()
            return Response(status=200,data={"message":"Profile created successfully","data":profile.data})
    
class LoginView(CreateAPIView):

    serializer_class=LoginViewSerializer
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
        
class ProfileUpdateDeleteAPIview(RetrieveUpdateDestroyAPIView):
    serializer_class=ProfileSerializer
    queryset=Profile.objects.all()
    permission_classes=[IsAuthenticated]
    def patch(self, request, *args, **kwargs):
        try:
            userprofile=Profile.objects.get(user=request.user)
            serializer=ProfileSerializer(userprofile,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=200,data=serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_206_PARTIAL_CONTENT,data={"error":str(e)})