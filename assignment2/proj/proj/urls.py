"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from proj_app import views

urlpatterns = [    
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('add/supervisor/', views.add_supervisor),
    path('add/supervisor/done/', views.add_supervisor_submit),
    re_path(r'^edit/supervisor/(?P<key>\w+)?/?$', views.modify_supervisor),
    re_path(r'^delete/supervisor/(?P<key>\w+)?/?$', views.modify_supervisor),

    path('groups/new/', views.group_create, name='group_create'),
    path('groups/<int:pk>/edit/', views.group_update, name='group_update'),
    path('topics/new/', views.topic_create, name='topic_create'),
    path('topics/<int:pk>/edit/', views.topic_update, name='topic_update'),
    path('applications/new/', views.application_create, name='application_create'),
    path('applications/<int:pk>/edit/', views.application_update, name='application_update'),

    # path('about/', views.about, name='about'),
    # path('project-list/', views.proj_list, name='proj-list'),
    # path('project/<int:topic_id>/', views.project_details, name='project_details'),

    
]
