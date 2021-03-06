from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     views = {}
#     views['feedbacks'] = Review.objects.all()
#     return render(request,'index.html', views)



def home(request):
    views = {}
    views['feedbacks'] = Review.objects.all()
    # views['projects'] = Project.object.all()
    return render(request,'index.html', views)

def about(request):
    views = {}
    # views['feedbacks'] = Review.objects.all()
    views['skills'] = Skills.objects.all()
    return render(request,'about.html',views)

def blog_home(request):
    return render(request,'blog-home.html')

def blog_single(request):
    return render(request,'blog-single.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
    return render(request,'contact.html')

def elements(request):
    return render(request,'elements.html')

def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    return render(request,'price.html')

def services(request):
    return render(request,'services.html')





