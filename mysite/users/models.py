from django.db import models

# Create your models here.

class IPregistradas(models.Model):
    ip=models.CharField(max_length=200)
    visita = models.DateTimeField(auto_now_add=True)
