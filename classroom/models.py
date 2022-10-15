from tkinter import TRUE
from django.db import models

# Create your models here.



#Creating classroom model 
class classroom(models.Model):
    #<--uncomment when user model is created-->
    #t_id=models.ForeignKey(user,on_delete=models.cascade)
    c_id=models.AutoField(primary_key=TRUE)
    subject=models.CharField(max_length=100)
    ilink=models.CharField(max_length=5000)
    cname=models.CharField(max_length=500)
    about=models.CharField(max_length=5000)



