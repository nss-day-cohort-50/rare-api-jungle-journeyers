from django.db import models

class Categories(models.Model):
<<<<<<< HEAD
    label = models.TextField()
=======
    label = models.CharField(max_length=55)
>>>>>>> main
