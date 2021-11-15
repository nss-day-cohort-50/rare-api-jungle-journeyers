from django.db import models


class Comments(models.Model):
    content = models.TextField()
    created_on = models.DateField()
    post = models.ForeignKey("Posts", on_delete=models.CASCADE)
    author = models.ForeignKey("RareUser", on_delete=models.CASCADE)