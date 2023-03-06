from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from . models import Branches,Details
from .forms import DetailsForm
# Create your views here.
def index(request,):
    branches = Branches.objects.all()
    return render(request,'home.html',{'branches':branches})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,"Invalid username or Password")
            return redirect('/login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if password != confirm_password:
            messages.info(request,'Password does not match')
            return redirect('/register')
        elif User.objects.filter(username=user_name).exists():
            messages.info(request,'Username already used')
            return redirect('/register')
        else:
            user = User.objects.create_user(username=user_name,password=password)
            user.save()
            return redirect('/login')
    else:    
        return render(request,'register.html')

def details_client(request):
    form = DetailsForm()
    branches = Branches.objects.all()
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'details.html', {'form': form,'branches':branches})

def load_branches(request):
    district_id = request.GET.get('district_id')
    branchess = Branches.objects.filter(district_id=district_id).order_by('branch')
    return render(request, 'branches_dropdown_list_options.html', {'branchess': branchess})