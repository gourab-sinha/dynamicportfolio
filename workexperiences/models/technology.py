from django.db import models
from profiles.models import SkillType

class Technology(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    TYPE = (
        (SkillType.PROGRAMMING_LANGUAGE, 'Programming Language'),
        (SkillType.WEB_FRAMEWORK, 'Web Framework'),
        (SkillType.VERSION_CONTROL, 'Version Control'),
        (SkillType.ALGORITHM, 'DS and Algorithm'),
        (SkillType.BACKEND_FRAMEWORK, 'Backend Framework'),
        (SkillType.DESIGN, 'Design'),
        (SkillType.OTHER, 'Other'),
    )
    tech_type = models.CharField(max_length=50, choices=TYPE)

    def __str__(self):
        return self.name