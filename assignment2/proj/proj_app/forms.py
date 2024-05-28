from django import forms
from .models import *

class SupervisorForm(forms.ModelForm) :
    class Meta:
        model = Supervisor
        fields = ['name', 'staffID', 'email']
        labels ={ 
            'staffID': 'Staff ID'
        }
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topicID', 'title', 'description', 'supervisor']

class GroupForm(forms.ModelForm) :
    class Meta:
        model = Supervisor
        fields = ['name', 'groupID', 'email']
        labels ={ 
            'groupID': 'Group ID'
        }


class ApplicationForm(forms.ModelForm) :
    class Meta:
        model = Application
        fields =['groupID', 'topicID']
        labels ={ 
            'groupID': 'Group ID',
            'topicID': 'Topic Number'

        }