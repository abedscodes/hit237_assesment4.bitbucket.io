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
    title = models.CharField(max_length=90)
    description = models.CharField(max_length=800)
    category = models.CharField(max_length= 80)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True)
    group_limit = models.PositiveIntegerField()
    cas = models.BooleanField(default= False)
    syd = models.BooleanField(default= False)
    external = models.BooleanField(default= False)
    chem_eng = models.BooleanField(default= False)
    cns_eng = models.BooleanField(default= False)
    eee = models.BooleanField(default= False)
    mech_eng = models.BooleanField(default= False)
    cs = models.BooleanField(default= False)
    cyb_sec = models.BooleanField(default= False)
    data_sc = models.BooleanField(default= False)
    is_ds = models.BooleanField(default= False)
    seng = models.BooleanField(default= False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def remove_if_no_groups(self):
        if not self.group_set.exists(): #type: ignore
            self.delete()

class Group(models.Model):
    groupID = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=100)
    supervisors = models.ForeignKey(Supervisor, on_delete=models.DO_NOTHING)
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)  # Field to track if the group's thesis project is approved
    email = models.EmailField()

    def __str__(self):
        return self.name

class Application(models.Model):
    groupID = models.ForeignKey(Group, on_delete=models.CASCADE)
    topicID = models.ForeignKey(Topic, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return str(self.id) + " : " + str(self.groupID) + " applied for topic number " + str(self.topicID) # type: ignore
