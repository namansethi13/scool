from django.contrib import admin
from .models import BaseUser ,classroom, classroomUsers,assignmentUsers,submission

admin.site.register(BaseUser)
admin.site.register(classroom)
admin.site.register(classroomUsers)
admin.site.register(assignmentUsers)
admin.site.register(submission)