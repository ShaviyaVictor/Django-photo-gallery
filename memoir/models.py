from unicodedata import name
from django.db import models

# Create your models here.
class categories(models.Model) :
  name = models.CharField(max_length=30)

  def __str__(self) -> str:
      return self.name

  class Meta :
    ordering = ['-name']