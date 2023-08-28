from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ 
    
    path('',views.index,name='index'),
    path("about", views.about, name="about" ) ,
    path("blog", views.blog, name="blog" ) ,
    path("shop", views.shop, name="shop" ) ,
    path("gallery", views.gallery, name="gallery" ) ,
    path("contact", views.contact, name="contact" ) ,
    path("productspage", views.productspage, name="productspage" ) ,
    path("productsdetails", views.productsdetails, name="productsdetails" ) ,
    path("sanjana/", views.sanjana, name="sanjana" ) ,
    path("sanjana2/", views.sanjana2, name="sanjana2" ) ,
     
    
              
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
