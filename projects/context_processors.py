from projects.models import Project

def projects(request):
    projects = Project.objects.all()
    context = {}
    context['projects'] = projects
    return context