from projects.models import Project

def projects(request):
    projects = Project.objects.all()
    context = {}
    context['projects'] = projects
    print(context['projects'][0].image)
    return context