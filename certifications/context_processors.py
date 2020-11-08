from certifications.models import Certificate

def certificates(request):
    context = {}
    context['certificates'] = Certificate.objects.all()
    return context
