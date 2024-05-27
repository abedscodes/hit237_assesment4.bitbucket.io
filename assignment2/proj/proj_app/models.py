from django.db import models

# Create your models here.


class Supervisor(models.Model):
    staffID = models.CharField(max_length=7, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return str(self.staffID) + " : " + self.name

class Group(models.Model):
    groupID = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=100)
    supervisors = models.ManyToManyField(Supervisor)
    is_approved = models.BooleanField(default=False)  # Field to track if the group's thesis project is approved

    def __str__(self):
        return self.name
         

class Topic(models.Model):
    topicID = models.CharField(max_length=4, primary_key=True)
    title = models.CharField(max_length=200)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='theses')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Student(models.Model):
    studentID = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name