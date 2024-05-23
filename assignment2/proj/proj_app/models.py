from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


def validate_six_digits(value):
    if not (value.isdigit() and len(value) == 6):
        raise ValidationError(f'{value} must be exactly 6 digits')

def validate_max_three_digits(value):
    if not (value.isdigit() and len(value) <= 3):
        raise ValidationError(f'{value} must be a maximum of 3 digits')

class Supervisor(models.Model):
    staffID = models.CharField(max_length=6, primary_key=True, validators=[validate_six_digits])
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Group(models.Model):
    groupID = models.CharField(max_length=6, primary_key=True, validators=[validate_six_digits])
    name = models.CharField(max_length=100)
    supervisors = models.ManyToManyField(Supervisor, related_name='groups')

    def __str__(self):
        return self.name

class Thesis(models.Model):
    thesisID = models.CharField(max_length=3, primary_key=True, validators=[validate_max_three_digits])
    title = models.CharField(max_length=200)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, related_name='theses')
    groups = models.ManyToManyField(Group, related_name='theses')

    def __str__(self):
        return self.title

class Student(models.Model):
    studentID = models.CharField(max_length=6, primary_key=True, validators=[validate_six_digits])
    name = models.CharField(max_length=100)
    email = models.EmailField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name