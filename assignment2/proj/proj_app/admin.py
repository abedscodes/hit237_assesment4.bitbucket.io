from django.contrib import admin
from proj_app.models import *

# Register your models here.
myModels = [Supervisor, Group, Topic, Student]
admin.site.register(myModels)