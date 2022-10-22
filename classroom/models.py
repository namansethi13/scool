import uuid
from tkinter import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext as _
from .managers import UserManager





#create user model here 

class BaseUser(AbstractUser, PermissionsMixin):
    u_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_("username"), max_length=200, blank=True, null=True, editable=False)
    email = models.EmailField(_("email"), max_length=200, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(_("Email Verified"), default=False)
    is_active = models.BooleanField(default=False)
    auth_token=models.CharField(max_length=100,default="")
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS= []
    objects = UserManager()



#Creating classroom model 
class classroom(models.Model):
    #<--uncomment when user model is created-->
    t_id=models.ForeignKey(BaseUser,on_delete=models.CASCADE , null = True)
    c_id=models.AutoField(primary_key=True)
    subject=models.CharField(max_length=100)
    ilink=models.CharField(max_length=5000)
    cname=models.CharField(max_length=500)
    about=models.TextField()
    

class classroomUsers(models.Model):
        users = models.ManyToManyField(BaseUser)
        classroom = models.ForeignKey(classroom, on_delete=models.CASCADE)





#create assignment model here 

class assignment(models.Model):
    a_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=100)
    title =  models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    t_id = models.ForeignKey(BaseUser,on_delete=models.CASCADE , null = True)
    duedate = models.DateTimeField()

class assignmentUsers(models.Model):
        assigned_to = models.ManyToManyField(BaseUser)
        assignment = models.ForeignKey(assignment, on_delete=models.CASCADE)



class submission(models.Model):
    submitted_by = models.ForeignKey(BaseUser,on_delete=models.CASCADE , null = True)
    submission_date = models.DateTimeField()
    submission = models.CharField(max_length=5000)
    assignment = models.ForeignKey(assignment, on_delete=models.CASCADE)




