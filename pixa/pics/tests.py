from django.test import TestCase
from .models import Image,Location,Category


# Create your tests here.
class ImageTests(TestCase):
    
    # Setup method
    def setUp(self):
        self.location = Location(location='Africa')
        self.location.save()
        
        
        self.image = Image(image = 'pic.jpg', image_name='test',image_description='This is a test',location = self.location)
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        
        
        
    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
    def test_save_image(self):
        self.image = Image(image = 'pic.jpg', image_name='test',image_description='This is a test',location = self.location)
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) >= 1)
    def test_delete_method(self):
        self.image = Image(image = 'pic.jpg', image_name='test',image_description='This is a test',location = self.location)
        self.image.save_image()
        images = self.image.delete_image()
        deleted = Image.objects.all()
        self.assertTrue(len(deleted) <= 0)
class Test_location(TestCase):
    
    def setUp(self):
        
        self.location = Location(location="Nairobi")
        
    def tearDown(self):
        Location.objects.all().delete()
        
    def test_save_location(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location)>= 1)
        
    def test_delete_location(self):
        self.location.save_location()
        locations = self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) <= 0)
class Test_category(TestCase):
     
    def setUp(self):
        self.category = Category(category="Fun")
        
    def tearDown(self):
        Category.objects.all().delete()
        
    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>= 1)
        
    def test_delete_category(self):
        self.category.save_category()
        categories = self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) <= 0)

