# Generated by Django 4.0.3 on 2022-10-16 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='assignment',
            fields=[
                ('a_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
                ('duedate', models.DateTimeField()),
                ('t_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateTimeField()),
                ('submission', models.CharField(max_length=5000)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.assignment')),
                ('submitted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='assignmentUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_to', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.assignment')),
            ],
        ),
    ]