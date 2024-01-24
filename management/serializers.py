from rest_framework import serializers
from management import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Projects
        fields="__all__"
    def validate(self, data):
        if data.get('planned_start_date') > data.get('planned_end_date') or data.get('actual_start_date') > data.get('actual_end_date'):
            raise serializers.ValidationError("End date must greater than Start date")
        return super().validate(data)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tag
        fields="__all__"

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Sprints
        fields="__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tasks
        fields="__all__"

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Status
        fields="__all__"

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Comments
        fields="__all__"

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Notes
        fields="__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Client
        fields="__all__"

class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.TechStack
        fields="__all__"