from django.urls import path
from projects.views.project_home import ProjectHome

app_name = 'project'
urlpatterns = [
    path('projects/', ProjectHome.as_view(), name='projects')
]