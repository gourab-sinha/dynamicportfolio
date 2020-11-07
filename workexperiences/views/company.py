from django.shortcuts import render
from django.views.generic import TemplateView

class CompanyView(TemplateView):
    template_name = 'companies/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})