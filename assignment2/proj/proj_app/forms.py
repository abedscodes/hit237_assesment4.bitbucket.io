from django import forms
from .models import Supervisor

class SupervisorForm(forms.ModelForm) :
    class Meta:
        model = Supervisor
        fields = ['name', 'staffID', 'email']
        labels ={ 
            'staffID': 'Staff ID'
        }