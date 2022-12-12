from django.db import models


# Create your models here.
class Profile(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    body=models.TextField()

    def __str__(self):
        return self.title;

    def trimbody(self):
        return self.body[:50]+"..."