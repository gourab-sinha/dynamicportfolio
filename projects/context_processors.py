from projects.models import Project

def projects(request):
    projects = Project.objects.all().order_by('-id')
    context = {}
    context['projects'] = projects
    return context