from django.db import models
from profiles.models import Skill, Achievement
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=100, blank=False)
    bio = models.TextField(blank=True)
    skills = models.ManyToManyField(Skill)
    achievements = models.ManyToManyField(Achievement)
    slug = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name

    @property
    def skills_set(self):
        return [skill for skill in self.skills.all()]

    @property
    def achievement_list(self):
        return [achievement for achievement in self.achievements.all()]