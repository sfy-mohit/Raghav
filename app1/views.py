from django.shortcuts import render
from .models import Service
from .models import Banner
from .models import Product
from .models import Product2
from .models import Gallery
from .models import Sidebanner
from .models import Member
from .models import News
from .models import Feature
from .models import Achievement
from .models import ContactForm


# Create your views here.

def index(request):
    servicesData=Service.objects.all()
    bannersData=Banner.objects.all()
    productsData = Product.objects.all()[:4]
    galleryData = Gallery.objects.all()[:8]
    sidebannersData = Sidebanner.objects.all()
    memberData = Member.objects.all()
    newsData = News.objects.all()
    featureData = Feature.objects.all()
    Context = { 
            'sidebannersData':sidebannersData,
            'servicesData':servicesData,
            'bannersData':bannersData,
            'productsData':productsData,
            'galleryData':galleryData,
            'memberData':memberData,
            'newsData':newsData,
            'featureData':featureData,
            
             
         }
    return render(request,"index.html",Context)

def about(request):
    featureData = Feature.objects.all()
    memberData = Member.objects.all()
    achievementData = Member.objects.all()
    Context = { 
            
            'featureData':featureData,
            'memberData':memberData,
            'achievementData':achievementData,

         }
    return render(request,"about.html",Context)

def blog(request):
    return render(request,"blog.html")

def shop(request):
    return render(request,"shop.html")

def productspage(request):
    productsData = Product.objects.all()
    Context = { 
           
            'productsData':productsData,
             
         }
    return render(request,"product-page.html",Context)

def productsdetails(request):
    return render(request,"product-single.html")

def gallery(request):
    galleryData = Gallery.objects.all()
    Context = { 
            'galleryData':galleryData,
             
         }
    
    return render(request,"gallery-2.html",Context)

def contact(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_data = ContactForm(username=username, email=email, subject=subject, message=message)
        contact_data.save()
        Context = {
        'username':username       
        }
        return render(request,'contact.html',Context)
    else:
        return render(request,'contact.html')
        
        
def sanjana(request):
    product2Data = Product2.objects.all()
    featureData = Feature.objects.all()
    galleryData = Gallery.objects.all()
    newsData = News.objects.all()
    productsData = Product.objects.all()  
    
    Context = { 
            ''
            'product2Data':product2Data,
            'featureData':featureData,
            'galleryData':galleryData,
            'newsData':newsData,
            'productsData':productsData,
            
         }
    return render(request,"sanjanaorg.html",Context)

def sanjana2(request):
    product2Data = Product2.objects.all()
    featureData = Feature.objects.all()
    galleryData = Gallery.objects.all()
    productsData = Product.objects.all()  
    
    Context = { 
            ''
            'product2Data':product2Data,
            'featureData':featureData,
            'galleryData':galleryData,
            'productsData':productsData,
            
         }
    return render(request,"sanjana-agro.html",Context)








