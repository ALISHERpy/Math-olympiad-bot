from django.db import models

# Create your models here.

class IMAGES(models.Model):
    file_id=models.CharField(max_length=300)
    description=models.TextField(blank=True)
    def __str__(self):
        return f"{self.file_id[:5]} : {self.description[:5]}"

class VIDEOS(models.Model):
    file_id=models.CharField(max_length=300)
    description=models.TextField(blank=True)
    def __str__(self):
        return f"{self.file_id[:5]} : {self.description[:5]}"

class TestFile(models.Model):
    file_id=models.CharField(max_length=300)
    description=models.TextField(blank=True)
    def __str__(self):
        return f"{self.file_id[:5]} : {self.description[:5]}"
