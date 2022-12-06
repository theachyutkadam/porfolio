from django.db import models
#DataFlair Models
class ProjectDetails(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    technology = models.CharField(max_length = 30, default='html')
    description = models.TextField(default = 'DataFlair Django tutorials')
    def __str__(self):
        return self.name
