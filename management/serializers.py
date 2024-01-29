from rest_framework import serializers
from management import models
import contextlib

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Project
        fields="__all__"
    def validate(self, data):
        if data.get('planned_start_date') <= data.get('planned_end_date') or data.get('actual_start_date') <= data.get('actual_end_date'):
            return super().validate(data)
        raise serializers.ValidationError("End date must greater than Start date")
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tag
        fields="__all__"

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Sprint
        fields="__all__"

class TaskSerializer(serializers.ModelSerializer):
    sprintname=serializers.CharField(source="sprint.sprintname",required=False)
    projectname=serializers.CharField(source="sprint.project.projectname",required=False)
    ownername=serializers.CharField(source="owner.username",required=False)
    class Meta:
        model=models.Task
        fields='__all__'
    
    
    def validate(self, attrs):
        try:
            project=models.Sprint.objects.get(pk=attrs.get('sprint').id,project__stakeholders__in=[attrs.get('owner')])
            if project:
                return super().validate(attrs)
        except Exception as e:
            print(e)
            raise serializers.ValidationError(detail="User not assigned to project")
        

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Status
        fields="__all__"

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Comment
        fields="__all__"

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Note
        fields="__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Client
        fields="__all__"

class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.TechStack
        fields="__all__"

class TimeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.TimeReport
        fields="__all__"