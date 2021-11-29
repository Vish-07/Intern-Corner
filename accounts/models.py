from django.db import models

# Create your models here.
class InternCorner(models.Model):
    Company =models.CharField(max_length=100)
    Position = models.CharField(max_length=30)
    Experience=models.TextField()
    Approve=models.BooleanField(default=False)
    Username=models.CharField(max_length=150)
