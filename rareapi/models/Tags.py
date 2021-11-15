from django.db import models

class Tags(models.Model):
    label = models.TextField()
    