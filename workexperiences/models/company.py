from django.db import models
from workexperiences.models import Technology, CompanyProject


class Company(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    team = models.CharField(max_length=50, blank=False, null=False)
    role = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='company/', blank=True)
    joining_date = models.DateField()
    ending_date = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(default=True)
    techs = models.ManyToManyField(Technology, blank=True)
    projects = models.ManyToManyField(CompanyProject, blank=True)
    slug = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name

    @property
    def list_projects(self):
        return reversed([project for project in self.projects.all()])

    @property
    def list_techs(self):
        return [tech for tech in self.techs.all()]
