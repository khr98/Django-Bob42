# Generated by Django 4.0.2 on 2022-05-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('idgroup', models.IntegerField(db_column='idGroup', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Relativetask',
            fields=[
                ('idrelativetask', models.IntegerField(db_column='idRelativeTask', primary_key=True, serialize=False)),
                ('relative_task', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'RelativeTask',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('idreservation', models.IntegerField(db_column='idReservation', primary_key=True, serialize=False)),
                ('date', models.DateTimeField(db_column='date')),
                ('time', models.IntegerField(db_column='time')),
            ],
            options={
                'db_table': 'Reservation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('idtodolist', models.IntegerField(db_column='idTodoList', primary_key=True, serialize=False)),
                ('task', models.CharField(max_length=45)),
                ('is_complete', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('region', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'TodoList',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('iduser', models.IntegerField(db_column='idUser', primary_key=True, serialize=False)),
                ('intraid', models.CharField(db_column='intraID', max_length=45)),
                ('name', models.CharField(db_column='name', max_length=45)),
                ('phone', models.CharField(blank=True, db_column='phone', max_length=45, null=True)),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
    ]
