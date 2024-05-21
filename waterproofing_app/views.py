from django.shortcuts import render, redirect
from .models import Service, Inquiry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    return render(request, 'register.html', {'form': form})


def services(request):
    services = Service.objects.all()
    print(services)  
    return render(request, 'services.html', {'services': services})



@login_required
def submit_inquiry(request, service_id):
    if request.method == 'POST':
        message = request.POST.get('message')
        service = Service.objects.get(pk=service_id)
        inquiry = Inquiry(customer=request.user, service=service, message=message)
        inquiry.save()
        return redirect('services')
    else:
        return render(request, 'submit_inquiry.html', {'service_id': service_id})
    
@login_required
def admin_dashboard(request):
    services = Service.objects.all()
    inquiries = Inquiry.objects.all()
    context = {
        'services': services,
        'inquiries': inquiries,
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def customer_dashboard(request):
    inquiries = Inquiry.objects.filter(customer=request.user)
    context = {
        'inquiries': inquiries
    }
    return render(request, 'customer_dashboard.html', context)

from django.contrib.admin.views.decorators import staff_member_required

@login_required
def user_dashboard(request):
    inquiries = Inquiry.objects.filter(user=request.user)
    context = {
        'inquiries': inquiries,
    }
    return render(request, 'user_dashboard.html')

@staff_member_required
def admin_dashboard(request):
    services = Service.objects.all()
    inquiries = Inquiry.objects.all()
    context = {
        'services': services,
        'inquiries': inquiries,
    }
    return render(request, 'admin_dashboard.html')
