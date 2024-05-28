from django.db import models

# Create your models here.

class Supervisor(models.Model):
    staffID = models.CharField(max_length=7, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return str(self.staffID) + " : " + self.name

class Topic(models.Model):
    topicID = models.CharField(max_length=4, primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField()
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def remove_if_no_groups(self):
        if not self.group_set.exists():
            self.delete()

class Group(models.Model):
    groupID = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=100)
    supervisors = models.ManyToManyField(Supervisor)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)  # Field to track if the group's thesis project is approved
    email = models.EmailField()

    def __str__(self):
        return self.name

class Application(models.Model):

    groupID = models.ForeignKey(Group, on_delete=models.CASCADE)
    topicID = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " : " + str(self.groupID) + " applied for topic number " + str(self.topicID)
