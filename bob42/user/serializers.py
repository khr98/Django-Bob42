from dataclasses import fields
from rest_framework import serializers
from .models import User,Reservation,Group,Todolist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('idUser','intraid','name','phone')
  
class ReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model=Reservation
		fields=('idreservation','date','time','user_iduser')
  
class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model=Group
		fields=('idgroup','reservation_idreservation')
  
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todolist
        fields= '__all__'