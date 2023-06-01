from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(verbose_name="Image", upload_to="projects")
    link = models.URLField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Modification Date")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-created"]

    def __str__(self):
        return self.title