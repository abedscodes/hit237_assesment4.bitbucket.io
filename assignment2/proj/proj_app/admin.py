from django.contrib import admin
from proj_app.models import *

# Register your models here.
myModels = [Supervisor, Group, Topic, Application]
admin.site.register(myModels)