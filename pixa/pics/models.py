from django.db import models
 

class Category(models.Model):
    
    category = models.CharField(max_length =20)
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
    
    
    def __str__(self):
        return self.category
    


class Location(models.Model):
    location=models.CharField(max_length=30)
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.location


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField(max_length=5000)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
@classmethod
# 
def search_by_category(cls,category):
    categories = cls.objects.filter(category)
    return categories
    
@classmethod
def get_image_by_id(cls, id):
    images = cls.objects.filter(location=location)
    return images
    
@classmethod
def filter_by_location(cls, location):
    images = cls.objects.filter(location=location)
    return images
@classmethod
def update_image(cls, id):
    images = cls.objects.filter(id=id).update(id=id)
    return images
    
def __str__(self):
    return self.image_name



    
   
    
    
    