from django.db import models

#Sign up Form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.

#home page or product page product section

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

# home page or gallery section image gallery

class Gallery(models.Model):
      
      image = models.ImageField(upload_to='app1/media/gallery')
      

# sanjana organic image gallery

class Galleryso(models.Model):
      
      image = models.ImageField(upload_to='app1/media/galleryso')
      
# sanjana agrovate image gallery

class Gallerysa(models.Model):
      
      image = models.ImageField(upload_to='app1/media/gallerysa')        

     
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

# # FOR USER REGISTRATION-1 this is not in use

class Signup(models.Model):
      name = models.CharField(max_length=50)
      mobile = models.CharField(max_length=50,null=True,blank=True)
      email1 = models.EmailField(max_length=50,null=True,blank=True)
      username = models.CharField(max_length=50)
      pass1 = models.CharField(max_length=50)
      pass2 = models.CharField(max_length=50)
      
      def __str__(self):
        return self.username

# website login 

class Login(models.Model):
      username = models.CharField(max_length=50)
      password = models.CharField(max_length=50)
      
      def __str__(self):
        return self.username
  
# Sign up form user registration 2 ( use mai yahi hai)

class SignupForm(UserCreationForm):
      first_name = forms.CharField(max_length = 20)
      last_name = forms.CharField(max_length = 20)
      email = forms.EmailField()
      phone_no = forms.CharField(max_length = 20)
      
      
      class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_no', 'email', 'username', 'password1', 'password2']
        
        
# class UserProfile(models.Model):
#       user = models.OneToOneField(User, on_delete=models.CASCADE)
#       signupForm = models.ForeignKey(SignupForm, on_delete=models.CASCADE)
              
#       # user = models.ForeignKey(SignupForm , on_delete=CASCADE)
#       # name = models.CharField(max_length=50)
#       # mobile = models.CharField(max_length=50,null=True,blank=True)
#       # email = models.EmailField(max_length=50,null=True,blank=True)
#       # username = models.CharField(max_length=50)
#       # address = models.CharField(max_length=150)
      
#       def __str__(self):
#         return self.user        



# sanjana orhganics product

class Product3(models.Model):

    product_name = models.CharField(max_length=70)    
    product_des = models.TextField()
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    del_price = models.CharField(max_length=50)
    pub_date = models.DateField()
    Product_image = models.ImageField(upload_to='app1/media/product3')
    Product_icon = models.ImageField(upload_to='app1/media/product3')
    last_modified = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.product_name