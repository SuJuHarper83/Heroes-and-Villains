from django.db import models

# Create your models here.
# As a developer, I want to create a SuperType model in a “super_types” app.
# Property names must be in snake_case and match the following exactly!
# type – CharField

class SuperType(models.Model):
    type = models.CharField(max_length=225)
    
