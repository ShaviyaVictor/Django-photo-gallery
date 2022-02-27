from django.utils import timezone
from django.db import models
from django.forms import ImageField
from django.contrib.auth.models import User

# Create your models here.
class categories(models.Model) :
  name = models.CharField(max_length=30)

  def __str__(self) -> str:
      return self.name

  class Meta :
    ordering = ['-name']



class photos(models.Model) :
  img_title  = models.CharField(max_length=100)
  img_description = models.TextField()
  image = models.ImageField(upload_to='Images/')
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  img_categories = models.CharField(max_length=255)


  def __str__(self) -> str:
      return self.img_title

  class Meta :
    ordering = ['-img_title']