from tkinter import TRUE
from django.db import models




#create user model here 







#Creating classroom model 
class classroom(models.Model):
    #<--uncomment when user model is created-->
    #t_id=models.ForeignKey(user,on_delete=models.CASCADE)
    c_id=models.AutoField(primary_key=True)
    subject=models.CharField(max_length=100)
    ilink=models.CharField(max_length=5000)
    cname=models.CharField(max_length=500)
    about=models.TextField()
    



#create assignment model here 



