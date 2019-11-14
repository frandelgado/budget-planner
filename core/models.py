from django.db import models

# Create your models here.
class TimestampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)