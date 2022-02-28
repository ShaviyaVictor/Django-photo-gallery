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