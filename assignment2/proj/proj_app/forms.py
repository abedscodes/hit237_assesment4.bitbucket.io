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
        fields = ['topicID', 'title', 'description', 'category', 'supervisor', 'cas','syd', 'external',
                  'chem_eng', 'cns_eng', 'eee', 'mech_eng', 'cs', 'cyb_sec',
                  'data_sc', 'is_ds', 'seng']
        labels = {
            'cas': 'Internal - Casuarina',
            'syd': 'Internal - Sydney',
            'ext': 'External',
            'chem_eng': 'Chemical Engineering',
            'cns_eng': 'Civil and Structural Engineering',
            'eee': 'Electrical and Electronics Engineering',
            'mech_eng': 'Mechanical Engineering',
            'cs': 'Computer Science',
            'cyb_sec': ' Cyber Security',
            'data_sc': 'Data Science',
            'is_ds': 'Information Systems and Data Science',
            'seng': 'Software Engineering',
        }

class GroupForm(forms.ModelForm) :
    class Meta:
        model = Group
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