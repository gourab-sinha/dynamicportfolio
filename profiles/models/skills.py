from django.db import models
from enum import Enum

class SkillType:
    PROGRAMMING_LANGUAGE = "PROGRAMMING LANGUAGE"
    WEB_FRAMEWORK = "WEB FRAMEWORK"
    VERSION_CONTROL = "VERSION CONTROL"
    ALGORITHM = "ALGORIGHTM"
    BACKEND_FRAMEWORK = "BACKEND FRAMEWORK"
    DESIGN = "DESIGN"
    OTHER = "OTHER"

class Skill(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    TYPE = (
        (SkillType.PROGRAMMING_LANGUAGE, 'Programming Language'),
        (SkillType.WEB_FRAMEWORK, 'Web Framework'),
        (SkillType.VERSION_CONTROL, 'Version Control'),
        (SkillType.ALGORITHM, 'DS and Algorithm'),
        (SkillType.BACKEND_FRAMEWORK, 'Backend Framework'),
        (SkillType.DESIGN, 'Design'),
        (SkillType.OTHER, 'Other'),
    )
    skill_type = models.CharField(max_length=50, choices=TYPE)
    slug = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.title
