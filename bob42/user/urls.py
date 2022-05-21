from django.urls import path, include
from .views import HelloAPI, TaskDetailAPIView, TaskListAPIView, randomUser

urlpatterns = [
    path("hello/", HelloAPI),
    path("randomMatching/", randomUser),
    path("tasks/", TaskListAPIView.as_view()),
    path("tasks/<int:pk>", TaskDetailAPIView.as_view()),
]

