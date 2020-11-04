from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='projects/', default='projects/default.jpg')
    description = models.TextField(blank=False, null=False)
    verify_url = models.URLField()

    def __str__(self):
        return self.title