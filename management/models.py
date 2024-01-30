from typing import Any
from django.db import models
from accounts.models import User
# Create your models here.
class Tag(models.Model):
    tagname=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural="Tags"

    def __str__(self) -> str:
        return f"{self.tagname}"

class Status(models.Model):
    status=models.CharField(default="status",max_length=50)
    class Meta:
        verbose_name_plural="Status"

    def __str__(self) -> str:
        return f"{self.status}"

class Client(models.Model):
    clientname=models.CharField(max_length=100,default="client")
    class Meta:
        verbose_name_plural="Clients"

    def __str__(self) -> str:
        return f"{self.clientname}"

class TechStack(models.Model):
    stackname=models.CharField(max_length=50)
    version=models.CharField(max_length=10)
    class Meta:
        verbose_name_plural="TechStacks"

    def __str__(self) -> str:
        return f"{self.stackname}-{self.version}"

class Project(models.Model):
    projectname=models.CharField(max_length=50,blank=False,null=False)
    owner=models.ForeignKey(User, related_name="projects",on_delete=models.CASCADE)
    completion=models.IntegerField(default=0)
    estimate=models.IntegerField(default=0)
    client=models.ForeignKey(Client, related_name="project", on_delete=models.DO_NOTHING,)
    duedate=models.DateField()
    status=models.ForeignKey(Status, related_name="project", on_delete=models.DO_NOTHING)
    type=models.CharField(max_length=10,null=True)
    stakeholders=models.ManyToManyField(User,related_name="project")
    planned_end_date=models.DateField(null=True)
    actual_end_date=models.DateField(null=True)
    planned_start_date=models.DateField(null=True)
    actual_start_date=models.DateField(null=True)
    total_cost=models.IntegerField()
    cost_incurred_percentage=models.FloatField(default=0)
    cost_incurred=models.IntegerField()
    cost_Exceeded=models.IntegerField()
    tags=models.ManyToManyField(Tag)
    techstack=models.ManyToManyField(TechStack)

    def __str__(self) -> str:
        return f"{self.projectname} - {self.owner.username} - {self.duedate}"

class Sprint(models.Model):
    project=models.ForeignKey(Project,related_name="sprints",on_delete=models.DO_NOTHING)
    sprintname=models.CharField(max_length=50)
    endson=models.DateField(null=True)

    def __str__(self) -> str:
        return f"{self.project.projectname} - {self.sprintname}"

class Task(models.Model):
    owner=models.ForeignKey(User,related_name="tasks",on_delete=models.DO_NOTHING,null=True)
    estimate=models.CharField(max_length=10,default='0 hr')
    taskname=models.CharField(max_length=50,)
    description=models.TextField(blank=True,null=True)
    status=models.ForeignKey(Status, related_name="tasks", on_delete=models.DO_NOTHING)
    sprint=models.ForeignKey(Sprint,related_name="tasks",on_delete=models.CASCADE,null=True)
    duedate=models.DateField(null=True)
    
    class Meta:
        verbose_name_plural='Tasks'
        verbose_name='Task'

    def __str__(self) -> str:
        return f"{self.taskname}-{self.sprint.sprintname}-{self.duedate}"
    
class Comment(models.Model):
    comments=models.CharField(default="comments",max_length=200)
    def __str__(self) -> str:
        return f"{self.comments}"

class Note(models.Model):
    notes=models.CharField(default="notes",max_length=100)
    
    def __str__(self) -> str:
        return f"{self.notes}"

class TimeReport(models.Model):
    task=models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    date=models.DateField(auto_now_add=True)
    hours=models.IntegerField(default=0)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"{self.date}-{self.hours}"

