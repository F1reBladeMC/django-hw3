from django.db import models

# Create your models here.
from django.db import models

class SiteSettings(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/')
    icon = models.ImageField(upload_to='icons/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    locate = models.CharField(max_length=255)

    def __str__(self):
        return self.title
