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


  def save_category(self) :
    self.save()


  def delete_category(self) :
    self.delete()



class location(models.Model) :
  name = models.CharField(max_length=30)

  def __str__(self) -> str:
      return self.name

  class Meta :
    ordering = ['-name']


  def save_location(self) :
    self.save()


  def delete_location(self) :
    self.delete()



class photos(models.Model) :
  img_title  = models.CharField(max_length=100)
  img_description = models.TextField()
  image = models.ImageField(upload_to='Images/')
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  img_categories = models.CharField(max_length=255)
  img_location = models.ManyToManyField(location)
  


  def __str__(self) -> str:
      return self.img_title

  class Meta :
    ordering = ['-img_title']



   # Using filter method __icontains
  @classmethod
  def search_by_title(cls, search_term) :
    photo = cls.objects.filter(title__icontains = search_term)

    return photo