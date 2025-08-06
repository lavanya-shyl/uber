from django.shortcuts import render, get_object_or_404, redirect
from .models import Ride
from .forms import RideForm
from .forms import CustomerForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def ride_list(request):
    rides = Ride.objects.all()
    return render(request, 'ride_list.html', {'rides': rides})



def add_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.calculate_fare()  # Sets fare and distance
            # Just to be safe, ensure fare is not None
            if ride.fare is None:
                ride.fare = 0
            ride.save()
            return redirect('ride_list')
    else:
        form = RideForm()
    return render(request, 'add_ride.html', {'form': form})


def edit_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)
    if request.method == 'POST':
        form = RideForm(request.POST, instance=ride)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.calculate_distance()
            ride.calculate_fare()
            ride.save()
            return redirect('ride_list')
    else:
        form = RideForm(instance=ride)
    return render(request, 'edit_ride.html', {'form': form})


def delete_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)
    ride.delete()
    return redirect('ride_list')



    
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
           name = form.cleaned_data['name']
           email = form.cleaned_data['email']
           phone = form.cleaned_data['phone']
           print(f"Customer: {name}, {email}, {phone}")
           return redirect('add_ride')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})




def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # or wherever you want to go after login
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')