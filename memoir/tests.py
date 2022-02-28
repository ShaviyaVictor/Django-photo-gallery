from django.test import TestCase
from .models import categories, location, photos

# Create your tests here.
class categoriesTestClass(TestCase) :
  # Set up method
  def setUp(self) :
    self.top = categories(id='1')

  # Testing the instance
  def test_instance(self) :
    self.assertTrue(isinstance(self.top, categories))

  # Testing the save_method for the categories class
  def test_save_method(self) :
    self.top.save_category()
    category_list = categories.objects.all()
    self.assertTrue(len(category_list) > 0)

  # Testing the delete method
  def test_delete_method(self) :
    self.top.delete_category()
    category_list = categories.objects.all()
    self.assertTrue(len(category_list) -+1)



class locationTestClass(TestCase) :
  # Set up method
  def setUp(self) :
    self.top = location(id='1')

  # Testing the instance
  def test_instance(self) :
    self.assertTrue(isinstance(self.top, location))

  # Testing the save method for the location class
  def test_save_method(self) :
    self.top.save_location()
    location_list = location.objects.all()
    self.assertTrue(len(location_list) > 0)

  # Testing the delete method
  def test_delete_method(self) :
    self.top.delete_location()
    location_list = location.objects.all()
    self.assertTrue(len(location_list) -+1)