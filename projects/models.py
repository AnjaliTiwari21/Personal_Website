from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    image1 = models.FilePathField(path="/project_images", default=None, blank=True, null=True)
    image2 = models.FilePathField(path="/project_images", default=None, blank=True, null=True)
    image3 = models.FilePathField(path="/project_images", default=None, blank=True, null=True)
    image4 = models.FilePathField(path="/project_images", default=None, blank=True, null=True)
    image5 = models.FilePathField(path="/project_images", default=None, blank=True, null=True)

                                   