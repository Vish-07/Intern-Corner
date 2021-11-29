from django.shortcuts import render, redirect
from django.urls.conf import include
from .models import InternCorner
# Create your views here.

from django.contrib import messages
from django.contrib.auth.models import User, auth
#from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        interns = InternCorner.objects.filter(Approve=True).order_by('-id')[:2]
        username = request.user.username
        userexperiences = InternCorner.objects.filter(Username=username)
        return render(request, 'index.html', {'interns':interns, 'userexperiences':userexperiences})
    else:
        interns = InternCorner.objects.filter(Approve=True).order_by('-id')[:2]
        return render(request, 'index.html', {'interns':interns})

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email already exists.")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=" ")
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Please enter same password.')
            return redirect('register')        
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def registerExperience(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            companyName= request.POST['companyName']
            position = request.POST['position']
            experience=request.POST['experience']
            userName=request.user.username
            interns = InternCorner.objects.filter(Company=companyName,Position=position,Username=userName).exists()
            print(interns)

            if interns is False:
                exp = InternCorner(Company=companyName,Position=position,Experience=experience,Username=userName)
                if len(experience) >= 150:
                    exp.save()
                    messages.info(request, 'Your experience is submitted, our team will view and add it!')
                else:
                    messages.info(request, 'Please add atleast 150 characters.')
            else:
                messages.info(request, 'Your experience was already present, please edit!')
            #user = auth.authenticate(username=username, password=password)

        return render(request,'registerExperience.html')
    else:
        return redirect('login')

def experiences(request):
    if request.user.is_authenticated:
        interns = InternCorner.objects.all()
        return render(request,'experiences.html',{'interns':interns})
    else:
        return redirect('login')

def single(request,year):
    interns = InternCorner.objects.get(id=year)
    return render(request,'single.html',{'interns':interns})

def logout(request):
    auth.logout(request)
    return redirect('/')

def editExperience(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            companyName= request.POST['companyName']
            position = request.POST['position']
            experience=request.POST['experience']
            userName=request.user.username
            interns = InternCorner.objects.filter(Company=companyName,Position=position,Username=userName).exists()
            if interns:
               interns = InternCorner.objects.get(Company=companyName,Position=position,Username=userName)
               interns.Experience=experience
               interns.Approve = False
               interns.save()
               messages.info(request, 'Your experience is submitted, our team will view and add it!')
            else:
               messages.info(request, 'Invalid credentials.')
        return render(request,'editExperience.html')
    else:
         return redirect('login')

def deleteExperience(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            companyName= request.POST['companyName']
            position = request.POST['position']
            userName=request.user.username
            interns = InternCorner.objects.filter(Company=companyName,Position=position,Username=userName).exists()
            if interns:
               interns = InternCorner.objects.get(Company=companyName,Position=position,Username=userName)
               interns.delete()
               messages.info(request, 'Experience deleted successfully.')
            else:
               messages.info(request, 'Invalid credentials.')
        return render(request,'deleteExperience.html')
    else:
         return redirect('login')
def search(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            companyName= request.POST['search']
            interns = InternCorner.objects.filter(Company__icontains=companyName).exists()
            if interns:
                interns=InternCorner.objects.filter(Company__icontains=companyName)
            else:
                interns=InternCorner.objects.all()
                messages.info(request, 'Sorry, search item does not exist.')
        else:
           messages.info(request, 'invalid credentials')
           interns=InternCorner.objects.all()
        return render(request,'experiences.html',{'interns':interns})
    else:
         return redirect('login')
