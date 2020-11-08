from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class CertificateView(TemplateView):
    template_name='certificates/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
