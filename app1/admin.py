from django.contrib import admin

# Register your models here.

from .models import *


   
admin.site.register(Product)                       #For Home & Product page
admin.site.register(Product2)                     #For sanjana agrovate
admin.site.register(Product3)                     #For sanjana organics
admin.site.register(Banner)
admin.site.register(Service)
admin.site.register(Sidebanner)
admin.site.register(Gallery)                       # raghav
admin.site.register(Galleryso)                     # sanjana organics
admin.site.register(Gallerysa)                     # sanjana aggrovate
admin.site.register(Member)
admin.site.register(News)
admin.site.register(Feature)
admin.site.register(Achievement)
admin.site.register(ContactForm)                  #For Raghav Contact Form
admin.site.register(ContactForm1)                 #For Sanjana Organics Contact Form
admin.site.register(ContactForm2)                 #For Sanjana Aggrovat Contact Form
admin.site.register(Signup)                       #For Registration
admin.site.register(Login)  



