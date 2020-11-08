from django.db import models

class Achievement(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.title