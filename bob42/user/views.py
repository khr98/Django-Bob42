from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Todolist, User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, ReservationSerializer, GroupSerializer, TaskSerializer
from rest_framework.views import APIView
import random
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    return Response("Hello API!")


@api_view(['GET'])
def randomUser(request):
    totalUser = User.objects.all()  # 모델로 만들어진 객체를 모두 가져오기
    randomUser = random.sample(list(totalUser), 1)   # id는 랜덤으로 나올 개수
    serializer = UserSerializer(
        randomUser, many=True)  # 다양한 내용들에 대해 내부적으로도 직렬화
    return Response(serializer.data)


class TaskListAPIView(APIView):

    def get(self, request):
        queryset = Todolist.objects.all()

        if request.query_params:
            complete = request.query_params.get('complete', None)
            task = request.query_params.get('task', None)
            print(task)
            if (complete == "False"):
                queryset = queryset.filter(is_complete=False, task=task)
                serializer = TaskSerializer(queryset, many=True)
            else:
                queryset = queryset.filter(is_complete=True)
                serializer = TaskSerializer(queryset, many=True)
        else:
            serializer = TaskSerializer(Todolist.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# TodoList 내용, 수정, 삭제

class TaskDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Todolist, pk=pk)

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = TaskSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = TaskSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk, is_complete=True)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
