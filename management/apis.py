from rest_framework.permissions import (IsAuthenticated)
from rest_framework import generics
from management import serializers
from management.models import (Project,Tag,Sprint,Task, Status,Comment,Note,Client,TechStack,TimeReport)
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class ProjectAPIView(generics.ListCreateAPIView):
    serializer_class=serializers.ProjectSerializer
    permission_classes=[IsAuthenticated]
    queryset=Project.objects.all()
    
    def get_queryset(self):
            return (super().get_queryset() if self.request.user.is_superuser
                    else  super().get_queryset().filter(stakeholders__in=[self.request.user]))


    def list(self, request, *args, **kwargs):
        projects=self.get_queryset()
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
    queryset=Project.objects.all()
    
    def patch(self, request,pk,*args, **kwargs):
        project=get_object_or_404(Project,pk=pk)
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
    queryset=Sprint.objects.all()

    def get_queryset(self):
        return (super().get_queryset() if self.request.user.is_superuser 
                else super().get_queryset().filter(project__stakeholders__in=[self.request.user]))
    
    def list(self, request, *args, **kwargs):
        sprints=self.get_queryset()
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
    queryset=Sprint.objects.all()
    
    def patch(self, request,pk,*args, **kwargs):
        sprint=get_object_or_404(Sprint,pk=pk)
        serializer=serializers.SprintSerializer(request.data,sprint=sprint)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Sprint updated successfully"},status=status.HTTP_202_ACCEPTED),
        return Response(data={"errors":serializer.errors},status=status.HTTP_206_PARTIAL_CONTENT)

class TaskCreateAPIView(generics.ListCreateAPIView):
    serializer_class=serializers.TaskSerializer
    permission_classes=[IsAuthenticated]
    queryset=Task.objects.all()
    
    def get_queryset(self):
        return (super().get_queryset() if self.request.user.is_superuser 
                else super().get_queryset().select_related('sprint').
                filter(sprint__project__stakeholders__in=[self.request.user],owner=self.request.user) )
    
    def list(self, request, *args, **kwargs):
        tasks=self.get_queryset()
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
    queryset=Task.objects.all()
    
    def patch(self, request,pk,*args, **kwargs):
        task=get_object_or_404(Task,pk=pk)
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
    queryset=Comment.objects.all()
    
    def list(self, request, *args, **kwargs):
        comments=Comment.objects.all()
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
        comment=get_object_or_404(Comment,pk=pk)
        serializer=serializers.CommentsSerializer(request.data,comment=comment)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Status updated successfully"},status=status.HTTP_202_ACCEPTED),
        return Response(data={"errors":serializer.errors},status=status.HTTP_206_PARTIAL_CONTENT)
    
class NotesCreateAPIview(generics.ListCreateAPIView):
    serializer_class=serializers.NotesSerializer
    permission_classes=[IsAuthenticated]
    queryset=Note.objects.all()
    
    def list(self, request, *args, **kwargs):
        notes=Note.objects.all()
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
    queryset=Note.objects.all()
    
    def patch(self, request,pk,*args, **kwargs):
        note=get_object_or_404(Note,pk=pk)
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
    
class TechStackAPIView(generics.ListCreateAPIView):
    serializer_class=serializers.TechStackSerializer
    queryset=TechStack.objects.all()
    permission_classes=[IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        techstacks=TechStack.objects.all()
        serializer=serializers.TechStackSerializer(techstacks,many=True)
        return Response(data={"data":serializer.data,})
    
    def post(self, request, *args, **kwargs):
        serializer=serializers.TechStackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Techstack Created Successfully"})
        return Response(data={"message":serializer.errors})
class TechstackUpdateAPIview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.TechStackSerializer
    permission_classes=[IsAuthenticated]
    queryset=Client.objects.all()
    
    def patch(self, request,pk,*args, **kwargs):
        client=get_object_or_404(TechStack,pk=pk)
        serializer=serializers.TechStackSerializer(request.data,client=client)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data":serializer.data,"message":"Status updated successfully"},status=status.HTTP_202_ACCEPTED),
        return Response(data={"errors":serializer.errors},status=status.HTTP_206_PARTIAL_CONTENT)

class TimeReportCreateAPIView(generics.ListCreateAPIView):
    serializer_class=serializers.TimeReportSerializer
    queryset=TimeReport.objects.all()
    permission_classes=[IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        report=TimeReport.objects.filter(user=self.request.user)
        serialized=serializers.TimeReportSerializer(report,many=True)
        return Response(status=200,data=serialized.data)
    
    def create(self, request, *args, **kwargs):
        timereport=serializers.TimeReportSerializer(data=request.data)
        if timereport.is_valid():
            timereport.save()
            return Response(status=status.HTTP_201_CREATED,data={"data":timereport.data,"message":"Time report created"})
        return Response(status=status.HTTP_206_PARTIAL_CONTENT,data={"error":timereport.errors})

class TimeReportUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    def patch(self, request,pk,*args, **kwargs):
        timereport=get_object_or_404(TimeReport,pk=pk)
        updatimereport=serializers.TimeReportSerializer(timereport,request.data)
        if updatimereport.is_valid():
            updatimereport.save()
            return Response(status=status.HTTP_200_OK,data={"data":updatimereport.data,"message":"Timereport Updated successfully"})
        return Response(status=status.HTTP_206_PARTIAL_CONTENT,data={"error":updatimereport.errors})
#------------------#
# Filter Projects  #
#------------------#
class FilterProjectAPIview(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        ...