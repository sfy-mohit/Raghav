from django.db import models

# Create your models here.

class Product(models.Model):

    title = models.CharField(max_length=50)    
    product_name = models.CharField(max_length=70)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    del_price = models.CharField(max_length=50)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='app1/media/product')
    last_modified = models.DateTimeField(auto_now_add = True)
 
    def __str__(self):
        return self.product_name
    
class Banner(models.Model):
      banner_img = models.ImageField(upload_to ='app1/media/banner')
      title = models.CharField(max_length=50)
      subtitle = models.CharField(max_length=100)
      button_text = models.CharField(max_length=50)
      
      def __str__(self):
        return self.title
      
class Service(models.Model):
      service_icon = models.ImageField(upload_to='app1/media/service')
      service_title = models.CharField(max_length=50)
      service_des = models.TextField()
      
      def __str__(self):
        return self.service_title
      
class Gallery(models.Model):
      
      image = models.ImageField(upload_to='app1/media/gallery')
      
      
class Sidebanner(models.Model):
      
      title = models.CharField(max_length=50)
      desc = models.CharField(max_length=300)
      message = models.CharField(max_length=100)
      
class Member(models.Model):
      member_image = models.ImageField(upload_to='app1/media/team')
      member_name = models.CharField(max_length=50)
      member_designation = models.CharField(max_length=50)
      member_des = models.TextField()
      
      def __str__(self):
        return self.member_name
  
class News(models.Model):
      news_image = models.ImageField(upload_to='app1/media/news')
      news_title = models.CharField(max_length=50)
      news_des = models.TextField()
      
      def __str__(self):
        return self.news_title

class Feature(models.Model):
      feature_icon = models.ImageField(upload_to='app1/media/feature')
      feature_title = models.CharField(max_length=50)
      feature_des = models.TextField()
      
      def __str__(self):
        return self.feature_title
  
# for history section ion About Page 
class Achievement(models.Model):
      achievement_icon = models.ImageField(upload_to='app1/media/achievement')
      achievement_title = models.CharField(max_length=50)
      achievement_des = models.TextField()
      
      def __str__(self):
        return self.achievement_title
  
# for Raghav---
class ContactForm(models.Model):
      username = models.CharField(max_length=100)
      email = models.EmailField(max_length=50,null=True,blank=True)
      subject = models.CharField(max_length=50,null=True,blank=True)
      message = models.TextField(null=True,blank=True)
      
      def __str__(self):
        return self.username
  
# for Sanjana Organics---
class ContactForm1(models.Model):
      username1 = models.CharField(max_length=100)
      email1 = models.EmailField(max_length=50,null=True,blank=True)
      subject1 = models.CharField(max_length=50,null=True,blank=True)
      message1 = models.TextField(null=True,blank=True)
      
      def __str__(self):
        return self.username1
  
# for Sanjana Aggrovate--
class ContactForm2(models.Model):
      username2 = models.CharField(max_length=100)
      email2 = models.EmailField(max_length=50,null=True,blank=True)
      subject2 = models.CharField(max_length=50,null=True,blank=True)
      message2 = models.TextField(null=True,blank=True)
      
      def __str__(self):
        return self.username2    

# for Sanjana Aggrovate Page
class Product2(models.Model):

    product_name = models.CharField(max_length=70)    
    product_des = models.TextField()
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    del_price = models.CharField(max_length=50)
    pub_date = models.DateField()
    Product_image = models.ImageField(upload_to='app1/media/product2')
    Product_icon = models.ImageField(upload_to='app1/media/product2')
    last_modified = models.DateTimeField(auto_now_add = True)
 
    def __str__(self):
        return self.product_name