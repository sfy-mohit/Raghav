from django.shortcuts import redirect, render , HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .models import SignupForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required          # not access without login use for required login
from django.contrib import messages
from .models import Service
from .models import Banner
from .models import Product                                # raghav pro
from .models import Product2                               # sanjana aggrovate product
from .models import Product3                               # sasnjana organics product
from .models import Gallery                                # rahghav & gallery page
from .models import Galleryso                              # sanjana organics
from .models import Gallerysa                              # sanjana aggrovate
from .models import Sidebanner
from .models import Member
from .models import News
from .models import Feature
from .models import Achievement
from .models import ContactForm
from .models import ContactForm1
from .models import ContactForm2
from .models import Signup

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

# gallery for home page or gallery section

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
    product3Data = Product3.objects.all()
    servicesData=Service.objects.all()[8:12]
    gallerysoData = Galleryso.objects.all()
    newsData = News.objects.all()
    productsData = Product.objects.all()  
    print(product3Data)
    Context = { 
            ''
            'product3Data':product3Data,
            'servicesData':servicesData,
            'gallerysoData':gallerysoData,
            'newsData':newsData,
            'productsData':productsData,
            
         }
    return render(request,"sanjanaorg.html",Context)

# Sanjana Aggrovate Page

def sanjana2(request):
    product2Data = Product2.objects.all()
    servicesData=Service.objects.all()[4:8]
    gallerysaData = Gallerysa.objects.all()
    productsData = Product.objects.all()  
    print(product2Data)
    
    Context = { 
            'product2Data':product2Data,
            'servicesData':servicesData,
            'gallerysaData':gallerysaData,
            'productsData':productsData,
         }
    return render(request,"sanjana-agro.html",Context)

# this registration page is not in used 

def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email1 = request.POST.get('email')
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return render(request,"registration.html")

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return render(request,"registration.html")
        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return render(request,"registration.html")
         
        signup_data = Signup( name=name ,username=username, mobile=mobile ,email1=email1, pass1=pass1 , pass2=pass2)
        signup_data.save()
        Context = {
        'username':username,
        'name':name,
        'pass1':pass1       
        }
        return render(request,'registration.html',Context)
    else:
        return render(request,"registration.html")


# user login

def ulogin(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request , username=username ,password=password)    
        if user is not None:    # if user exist            
            login(request, user )
            messages.success(request,('You are logged in'))
            return redirect ('/')      # routes to 'index page' on successful login
        else:
            messages.warning(request,('Error logging in'))
            return redirect('ulogin')
    else:
        return render(request,'login.html')

# user logout 

def ulogout(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('/')

def forget(request):
    return render(request,"forget.html")


# user Profile page releted to registration2


@login_required(login_url='ulogin')                            # not access without login
def profile(request):   
    if request.user.is_authenticated:
        details = request.user
        return render(request,"profile.html",{'details':details })
    else:
        return render(request, 'registration2.html')
    
# fields = ['first_name', 'last_name', 'phone_no', 'email', 'username', 'password1', 'password2']


# Signup Form used registration page

def registration2(request):
    form = SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request,('Youre succesfully registered.Plz login for Continue'))
            return render(request,"login.html")
    context ={
        'form':form
    }
    return render(request, 'registration2.html',context)


        
  

