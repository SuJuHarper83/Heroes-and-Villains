from django.db import models
from super_types.models import SuperType

# Create your models here.
# As a developer, I want to create a Super model in a “supers” app.
# Property names must be in snake_case and match the following exactly!
# name - CharField
# alter_ego  - CharField
# primary_ability - CharField
# secondary_ability – CharField
# catchphrase – CharField
# super_type – ForeignKey

class Supers(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE)
