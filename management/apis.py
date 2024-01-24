from rest_framework.permissions import (IsAuthenticated)
from rest_framework import generics
from management import serializers
from management.models import (Projects,Tag,Sprints,Tasks, Status,Comments,Notes,Client)
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class ProjectAPIView(generics.ListCreateAPIView):
    serializer_class=serializers.ProjectSerializer
    permission_classes=[IsAuthenticated]
    queryset=Projects.objects.all()
    def list(self, request, *args, **kwargs):
        projects=Projects.objects.all()
        serializer=serializers.ProjectSerializer(projects,many=True)
        return Response(data={"data":serializer.data,})
    def post(self, request, *args, **kwargs):
        serializer=serializers.ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Project Created Successfully"})
        return Response(data={"message":serializer.errors})

class ProjectUpdateAPIview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.ProjectSerializer
    permission_classes=[IsAuthenticated]
    queryset=Projects.objects.all()
    def patch(self, request,pk,*args, **kwargs):
        project=get_object_or_404(Projects,pk=pk)
        serializer=serializers.ProjectSerializer(request.data,project=project)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Project updated successfully"},status=status.HTTP_202_ACCEPTED),
        return Response(data={"errors":serializer.errors},status=status.HTTP_206_PARTIAL_CONTENT)

class TagCreateAPIview(generics.ListCreateAPIView):
    serializer_class=serializers.TagSerializer
    permission_classes=[IsAuthenticated]
    queryset=Tag.objects.all()
    def list(self, request, *args, **kwargs):
        tags=Tag.objects.all()
        serializer=serializers.TagSerializer(tags,many=True)
        return Response(data={"data":serializer.data,})
    def post(self, request, *args, **kwargs):
        serializer=serializers.TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Tag Created Successfully"})
        return Response(data={"message":serializer.errors})

class TagUpdateAPIview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.TagSerializer
    permission_classes=[IsAuthenticated]
    queryset=Tag.objects.all()
    def patch(self, request,pk,*args, **kwargs):
        project=get_object_or_404(Tag,pk=pk)
        serializer=serializers.TagSerializer(request.data,project=project)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Tag updated successfully"},status=status.HTTP_202_ACCEPTED),
        return Response(data={"errors":serializer.errors},status=status.HTTP_206_PARTIAL_CONTENT)

class SprintCreateAPIview(generics.ListCreateAPIView):
    serializer_class=serializers.SprintSerializer
    permission_classes=[IsAuthenticated]
    queryset=Sprints.objects.all()
    def list(self, request, *args, **kwargs):
        sprints=Sprints.objects.all()
        serializer=serializers.SprintSerializer(sprints,many=True)
        return Response(data={"data":serializer.data,})
    def post(self, request, *args, **kwargs):
        serializer=serializers.SprintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Sprint Created Successfully"})
        return Response(data={"message":serializer.errors})

class SprintsUpdateAPIview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.SprintSerializer
    permission_classes=[IsAuthenticated]
    queryset=Sprints.objects.all()
    def patch(self, request,pk,*args, **kwargs):
        sprint=get_object_or_404(Sprints,pk=pk)
        serializer=serializers.SprintSerializer(request.data,sprint=sprint)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Sprint updated successfully"},status=status.HTTP_202_ACCEPTED),
        return Response(data={"errors":serializer.errors},status=status.HTTP_206_PARTIAL_CONTENT)

class TaskCreateAPIview(generics.ListCreateAPIView):
    serializer_class=serializers.TaskSerializer
    permission_classes=[IsAuthenticated]
    queryset=Tasks.objects.all()
    def list(self, request, *args, **kwargs):
        tasks=Tasks.objects.all()
        serializer=serializers.TaskSerializer(tasks,many=True)
        return Response(data={"data":serializer.data,})
    def post(self, request, *args, **kwargs):
        serializer=serializers.TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Task Created Successfully"})
        return Response(data={"message":serializer.errors})

class TaskUpdateAPIview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.TaskSerializer
    permission_classes=[IsAuthenticated]
    queryset=Tasks.objects.all()
    def patch(self, request,pk,*args, **kwargs):
        task=get_object_or_404(Tasks,pk=pk)
        serializer=serializers.TaskSerializer(request.data,project=task)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Task updated successfully"},status=status.HTTP_202_ACCEPTED),
        return Response(data={"errors":serializer.errors},status=status.HTTP_206_PARTIAL_CONTENT)

class StatusCreateAPIview(generics.ListCreateAPIView):
    serializer_class=serializers.StatusSerializer
    permission_classes=[IsAuthenticated]
    queryset=Status.objects.all()
    def list(self, request, *args, **kwargs):
        status=Status.objects.all()
        serializer=serializers.StatusSerializer(status,many=True)
        return Response(data={"data":serializer.data,})
    def post(self, request, *args, **kwargs):
        serializer=serializers.StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Status Created Successfully"})
        return Response(data={"message":serializer.errors})

class StatusUpdateAPIview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.StatusSerializer
    permission_classes=[IsAuthenticated]
    queryset=Status.objects.all()
    def patch(self, request,pk,*args, **kwargs):
        status=get_object_or_404(Status,pk=pk)
        serializer=serializers.TaskSerializer(request.data,project=status)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Status updated successfully"},status=status.HTTP_202_ACCEPTED),
        return Response(data={"errors":serializer.errors},status=status.HTTP_206_PARTIAL_CONTENT)
    
class CommentsCreateAPIview(generics.ListCreateAPIView):
    serializer_class=serializers.CommentsSerializer
    permission_classes=[IsAuthenticated]
    queryset=Comments.objects.all()
    def list(self, request, *args, **kwargs):
        comments=Comments.objects.all()
        serializer=serializers.CommentsSerializer(comments,many=True)
        return Response(data={"data":serializer.data,})
    def post(self, request, *args, **kwargs):
        serializer=serializers.CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Comments Created Successfully"})
        return Response(data={"message":serializer.errors})

class CommentsUpdateAPIview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.CommentsSerializer
    permission_classes=[IsAuthenticated]
    queryset=Status.objects.all()
    def patch(self, request,pk,*args, **kwargs):
        comment=get_object_or_404(Comments,pk=pk)
        serializer=serializers.CommentsSerializer(request.data,comment=comment)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Status updated successfully"},status=status.HTTP_202_ACCEPTED),
        return Response(data={"errors":serializer.errors},status=status.HTTP_206_PARTIAL_CONTENT)
    
class NotesCreateAPIview(generics.ListCreateAPIView):
    serializer_class=serializers.NotesSerializer
    permission_classes=[IsAuthenticated]
    queryset=Notes.objects.all()
    def list(self, request, *args, **kwargs):
        notes=Notes.objects.all()
        serializer=serializers.NotesSerializer(notes,many=True)
        return Response(data={"data":serializer.data,})
    def post(self, request, *args, **kwargs):
        serializer=serializers.NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Status Created Successfully"})
        return Response(data={"message":serializer.errors})

class NotesUpdateAPIview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.NotesSerializer
    permission_classes=[IsAuthenticated]
    queryset=Notes.objects.all()
    def patch(self, request,pk,*args, **kwargs):
        note=get_object_or_404(Notes,pk=pk)
        serializer=serializers.NotesSerializer(request.data,note=note)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Status updated successfully"},status=status.HTTP_202_ACCEPTED),
        return Response(data={"errors":serializer.errors},status=status.HTTP_206_PARTIAL_CONTENT)
    

class ClientCreateAPIView(generics.ListAPIView):
    serializer_class=serializers.ClientSerializer
    permission_classes=[IsAuthenticated]
    queryset=Client.objects.all()
    def list(self, request, *args, **kwargs):
        clients=Client.objects.all()
        serializer=serializers.ClientSerializer(clients,many=True)
        return Response(data={"data":serializer.data,})
    def post(self, request, *args, **kwargs):
        serializer=serializers.ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Client Created Successfully"})
        return Response(data={"message":serializer.errors})

class ClientUpdateAPIview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.NotesSerializer
    permission_classes=[IsAuthenticated]
    queryset=Client.objects.all()
    def patch(self, request,pk,*args, **kwargs):
        client=get_object_or_404(Client,pk=pk)
        serializer=serializers.ClientSerializer(request.data,client=client)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Status updated successfully"},status=status.HTTP_202_ACCEPTED),
        return Response(data={"errors":serializer.errors},status=status.HTTP_206_PARTIAL_CONTENT)