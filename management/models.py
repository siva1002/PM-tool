from django.db import models
from accounts.models import User
# Create your models here.
class Tag(models.Model):
    tagname=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.tagname}"

class Status(models.Model):
    status=models.CharField(default="status",max_length=50)

    def __str__(self) -> str:
        return f"{self.status}"

class Client(models.Model):
    clientname=models.CharField(max_length=100,default="client")

    def __str__(self) -> str:
        return f"{self.clientname}"

class Projects(models.Model):
    projectname=models.CharField(max_length=50,blank=False,null=False)
    owner=models.ForeignKey(User, related_name="projects",on_delete=models.CASCADE)
    completion=models.IntegerField(default=0)
    client=models.ForeignKey(Client, related_name="project", on_delete=models.DO_NOTHING,)
    duedate=models.DateField()
    status=models.ForeignKey(Status, related_name="project", on_delete=models.DO_NOTHING)
    type=models.CharField(max_length=10,null=True)
    planned_end_date=models.DateField(null=True)
    actual_end_date=models.DateField(null=True)
    planned_start_date=models.DateField(null=True)
    actual_start_date=models.DateField(null=True)
    total_cost=models.IntegerField()
    cost_incurred_percentage=models.FloatField(default=0)
    cost_incurred=models.IntegerField()
    cost_Exceeded=models.IntegerField()
    tags=models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f"{self.projectname} - {self.owner.username} - {self.duedate}"

class Sprints(models.Model):
    project=models.ForeignKey(Projects,related_name="sprints",on_delete=models.DO_NOTHING)
    sprintname=models.CharField(max_length=50)
    endson=models.DateField(null=True)

    def __str__(self) -> str:
        return f"{self.project.projectname} - {self.sprintname}"

class Tasks(models.Model):
    taskname=models.CharField(max_length=50,)
    status=models.ForeignKey(Status, related_name="tasks", on_delete=models.DO_NOTHING)
    sprint=models.ForeignKey(Sprints,related_name="tasks",on_delete=models.CASCADE,null=True)
    duedate=models.DateField(null=True)

    def __str__(self) -> str:
        return f"{self.taskname}-{self.sprint.sprintname}-{self.duedate}"
    


class Comments(models.Model):
    comments=models.CharField(default="comments",max_length=200)

    def __str__(self) -> str:
        return f"{self.comments}"

class Notes(models.Model):
    notes=models.CharField(default="notes",max_length=100)
    
    def __str__(self) -> str:
        return f"{self.notes}"
    

