from curses.ascii import US
from re import U
from django.contrib import admin
from .models import Group,User,Reservation,Todolist,Relativetask
# Register your models here.
admin.site.register(Group)
admin.site.register(User)
admin.site.register(Reservation)
admin.site.register(Todolist)
admin.site.register(Relativetask)