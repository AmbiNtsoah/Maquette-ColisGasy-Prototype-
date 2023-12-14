from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Colis
from .forms import ColisForm

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    colis_list = Colis.objects.all()
    return render(request, 'index.html', {'colis_list': colis_list})

def SignupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
       
        if password1 != password2:
            return HttpResponse("Your password and confirm password are not the same")
        else:
            my_user=User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect('login')
    
    return render (request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('pass')
        user=authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else: 
            return HttpResponse("<center><h1>Username or Password is incorrect</h1></center>")
        
    return render (request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def expedier(request):
    form = ColisForm()
    if request.method == 'POST':
        form = ColisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
        else:
            return HttpResponse(""" Something went wrong. Please reload the webpage by clicking <a href="{{url:'index'}}>Reload</a>" """)
    else:
        return render(request, 'expedier.html', {'form': form})

def accept(request, colis_id):
    colis = get_object_or_404(Colis, pk=colis_id)
    colis.conducteur_accepte = True
    colis.save()
    return redirect('index')

def refuse(request, colis_id):
    colis = get_object_or_404(Colis, pk=colis_id)
    colis.delete()
    return redirect('index')
