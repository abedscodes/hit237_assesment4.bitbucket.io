from django import forms
from .models import *

class SupervisorForm(forms.ModelForm) :
    class Meta:
        model = Supervisor
        fields = ['name', 'staffID', 'email']
        labels ={ 
            'staffID': 'Staff ID'
        }

class GroupForm(forms.ModelForm) :
    class Meta:
        model = Supervisor
        fields = ['name', 'groupID', 'email']
        labels ={ 
            'staffID': 'Staff ID'
        }


class StudentForm(forms.ModelForm) :
    class Meta:
        model = Supervisor
        fields = ['name', 'staffID', 'email']
        labels ={ 
            'staffID': 'Staff ID'
        }