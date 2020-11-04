from django.shortcuts import render
from django.views.generic import TemplateView
from projects.models import Project


class ProjectHome(TemplateView):
    template_name = "projects/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})