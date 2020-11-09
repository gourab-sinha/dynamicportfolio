from workexperiences.models import Company

def work_experiences(request):
    context = {}
    context['companies'] = Company.objects.all().order_by('-id')
    return context
