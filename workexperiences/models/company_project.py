from django.db import models
from workexperiences.models import Technology

class CompanyProject(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    reporting_manager = models.CharField(max_length=50, blank=False, null=False)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='company/projects/', blank=True)
    description = models.TextField(blank=False, null=False)
    verify_url = models.URLField(null=True, blank=True)
    slug = models.CharField(max_length=200,unique=True)
    tech_used = models.ManyToManyField(Technology, blank=True)

    def __str__(self):
        return self.title