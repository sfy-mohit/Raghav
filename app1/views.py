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
from .models import ContactForm1
from .models import ContactForm2


# Create your views here.

def index(request):
    servicesData=Service.objects.all()[:4]
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

# for Raghav Contact Form ---

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
    
# for Sanjana Organics Contact Form --- 
   
def sanjanaorg_contact(request):
    if request.method == 'POST':
        username1 = request.POST.get('name1')
        email1 = request.POST.get('email1')
        subject1 = request.POST.get('subject1')
        message1 = request.POST.get('message1')

        contact_data1 = ContactForm1(username1=username1, email1=email1, subject1=subject1, message1=message1)
        contact_data1.save()
        Context = {
        'username1':username1     
        }
        return render(request,'contact.html',Context)
    else:
        return render(request,'contact.html')
    
# for Sanjana Aggrovate Contact Form ---

def sanjanaagro_contact(request):
    if request.method == 'POST':
        username2 = request.POST.get('name2')
        email2 = request.POST.get('email2')
        subject2 = request.POST.get('subject2')
        message2 = request.POST.get('message2')

        contact_data2 = ContactForm2(username2=username2, email2=email2, subject2=subject2, message2=message2)
        contact_data2.save()
        Context = {
        'username2':username2     
        }
        return render(request,'contact.html',Context)
    else:
        return render(request,'contact.html')   
        
# Sanjana Organics Page 

def sanjana(request):
    product2Data = Product2.objects.all()
    servicesData=Service.objects.all()[8:12]
    galleryData = Gallery.objects.all()
    newsData = News.objects.all()
    productsData = Product.objects.all()  
    
    Context = { 
            ''
            'product2Data':product2Data,
            'servicesData':servicesData,
            'galleryData':galleryData,
            'newsData':newsData,
            'productsData':productsData,
            
         }
    return render(request,"sanjanaorg.html",Context)

# Sanjana Aggrovate Page

def sanjana2(request):
    product2Data = Product2.objects.all()
    servicesData=Service.objects.all()[4:8]
    galleryData = Gallery.objects.all()
    productsData = Product.objects.all()  
    
    Context = { 
            ''
            'product2Data':product2Data,
            'servicesData':servicesData,
            'galleryData':galleryData,
            'productsData':productsData,
            
         }
    return render(request,"sanjana-agro.html",Context)








