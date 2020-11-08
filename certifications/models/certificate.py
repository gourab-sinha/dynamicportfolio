from django.db import models
from profiles.models import SkillType, Skill

# Create your models here.
class Certificate(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    issued_by = models.CharField(max_length=50,null=False,blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    expire_date = models.DateField(null=True, blank=True)
    is_lifetime_valid = models.BooleanField(default=False)
    image = models.ImageField(upload_to='certificates/', blank=True)
    verify_url = models.URLField(null=True, blank=True)
    description = models.TextField(blank=True)
    skills = models.ManyToManyField(Skill)
    slug = models.CharField(max_length=200,unique=True)


    def __str__(self):
        return self.title

    @property
    def list_skills(self):
        return [skill for skill in self.skills.all()]