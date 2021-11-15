from django.db import models

class Posts(models.Model):
    user= models.ForeignKey('RareUser', on_delete=models.CASCADE)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.CharField(max_length=50)
    content = models.TextField()
    approved = models.BooleanField()
    
    
    
    