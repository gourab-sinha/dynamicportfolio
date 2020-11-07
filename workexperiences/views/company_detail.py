from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from workexperiences.models import Company

class CompanyDetailView(TemplateView):
    template_name = 'companies/company_detail.html'

    def get(self, request, *args, **kwargs):
        company_id = kwargs.get('company_id')
        company_detail = get_object_or_404(Company, id=company_id)
        context = {}
        context['company_detail'] = company_detail
        return render(request, self.template_name, context)