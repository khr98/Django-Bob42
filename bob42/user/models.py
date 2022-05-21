from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.


class Group(models.Model):
    # Field name made lowercase.
    idgroup = models.IntegerField(db_column='idGroup', primary_key=True)
    # Field name made lowercase.
    reservation_idreservation = models.ForeignKey(
        'Reservation', models.DO_NOTHING, db_column='Reservation_idReservation')

    class Meta:
        managed = False
        db_table = 'Group'


class Reservation(models.Model):
    # Field name made lowercase.
    idreservation = models.IntegerField(
        db_column='idReservation', primary_key=True)
    date = models.DateTimeField(db_column='date')
    time = models.IntegerField(db_column='time')
    # Field name made lowercase.
    user_iduser = models.ForeignKey(
        'User', models.DO_NOTHING, db_column='User_idUser')

    class Meta:
        managed = False
        db_table = 'Reservation'


class User(models.Model):
    # Field name made lowercase.
    idUser = models.IntegerField(db_column='idUser', primary_key=True)
    # Field name made lowercase.
    intraid = models.CharField(db_column='intraID', max_length=45)
    name = models.CharField(db_column='name', max_length=45)
    phone = models.CharField(
        db_column='phone', max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class Relativetask(models.Model):
    idrelativetask = models.IntegerField(db_column='idRelativeTask', primary_key=True)  # Field name made lowercase.
    relative_task = models.CharField(verbose_name='연관된 일',max_length=45)

    class Meta:
        managed = False
        db_table = 'RelativeTask'
        
    def __str__(self):
        return self.relative_task


class Todolist(models.Model):
    idtodolist = models.IntegerField(db_column='idTodoList', primary_key=True)  # Field name made lowercase.
    task = models.CharField(verbose_name='해야할 일',db_column='task',max_length=45)
    is_complete = models.BooleanField(verbose_name='완료 여부',db_column='is_complete',default=False)
    start_date = models.DateTimeField(verbose_name='시작일',db_column='start_date')
    end_date = models.DateTimeField(verbose_name='마감일',db_column='end_date')
    region = models.CharField(verbose_name='장소',db_column='region',max_length=45)
    rtask = models.ForeignKey('Relativetask', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TodoList'
    
    def __str__(self):
        return self.task
