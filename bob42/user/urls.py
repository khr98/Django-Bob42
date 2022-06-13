from django.urls import path, include
from .views import HelloAPI, TaskDetailAPIView, TaskListAPIView, randomUser,Seoul42LoginAPIView

urlpatterns = [
    path('', randomUser),
    path('tasks/', TaskListAPIView.as_view()),
    path('tasks/<int:pk>', TaskDetailAPIView.as_view()),
    path('accounts/42seoul/login/',Seoul42LoginAPIView.as_view()),
    #path('accounts/42seoul/callback', Seoul42LoginCallBackApi.as_view()),
]

