from django.db import models

class Libro(models.Model):
    title = models.CharField(max_length=255)
    netword = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
