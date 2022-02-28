from django.test import TestCase
from .models import categories, location, photos
from django.contrib.auth.models import User

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



class photosTestClass(TestCase) :
  # Set up methods
  def setUp(self) :

    # Creating a new category
    self.new_category = categories(name='nature')
    self.new_category.save_category()


    # Creating a new location
    self.new_location = location(name='Nairobi')
    self.new_location.save_location()


    # Creating a new photos instance
    self.new_photos = photos(img_title='Test', img_description='Testing to see the instance', img_categories=self.new_category)


    self.new_photos.save()

    self.new_photos.img_location.add(self.new_location)




  # def test_search_results(self) :
  #   search_term = 'Programming'
  #   photos_found = photos.search_by_title(search_term)

  #   self.assertTrue(len(photos_found) > 0)




  def tearDown(self) :
    categories.objects.all().delete()
    location.objects.all().delete()
    photos.objects.all().delete()