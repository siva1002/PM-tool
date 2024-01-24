from django.urls import path
from management import apis

urlpatterns = [
    path('project/',apis.ProjectAPIView.as_view()),
    path('project/<int:pk>',apis.ProjectUpdateAPIview.as_view()),
    path('tag',apis.TagCreateAPIview.as_view()),
    path("tag/<int:pk>",apis.TagUpdateAPIview.as_view()),
    path("sprints",apis.SprintCreateAPIview.as_view()),
    path("sprints/<int:pk>",apis.SprintsUpdateAPIview.as_view()),
    path("task/",apis.TaskCreateAPIview.as_view()),
    path("task/<int:pk>",apis.TaskUpdateAPIview.as_view()),
    path("status/<int:pk>",apis.StatusUpdateAPIview.as_view()),
    path("status/",apis.StatusCreateAPIview.as_view()),
    path("comment/<int:pk>",apis.CommentsCreateAPIview.as_view()),
    path("comment/",apis.CommentsUpdateAPIview.as_view()),
    path("client/<int:pk>",apis.ClientCreateAPIView.as_view()),
    path("client/",apis.ClientCreateAPIView.as_view()),
    path("notes/",apis.NotesCreateAPIview.as_view()),
    path("notes/<int:pk>",apis.NotesUpdateAPIview.as_view())
    

]