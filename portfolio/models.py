from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/media')
    Git_URL = models.URLField(blank=True)
    website_URL = models.URLField(blank=True)


    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=350)
    date = models.DateField()

    def __str__(self):
        return self.title


