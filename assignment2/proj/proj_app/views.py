from django.shortcuts import render

# Create your views here.

def about(request):
    context={
        'admin_list': create_admins(),
    }
    return render(request, 'proj_app/about.html', context)

def home(request):
    context = {}
    return render(request, 'proj_app/home.html', context)


def create_admins():
    the_list=[]

    the_list.append(Admin(361066,
                            'Moiz Ali'))
    the_list.append(Admin(361222,
                            'Muhammed Abed'))
    the_list.append(Admin(365145,
                            'Heshara Danathma Balasooriya Balasooriya Mudiyanselage'))
    the_list.append(Admin(365635,
                            'Gokul Ashok'))      
    return the_list


# Define Admin class
class Admin:
    def __init__(self, id, name):
        self.id = id
        self.name= name

    
    def __str__(self):
        return str(self.id) +", " + self.name