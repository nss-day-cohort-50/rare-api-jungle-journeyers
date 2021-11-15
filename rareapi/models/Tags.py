from django.db import models

class Tags(models.Model):
    label = models.TextField()
    posts = models.ManyToManyField("Posts", through="PostTags", related_name="tags")
    