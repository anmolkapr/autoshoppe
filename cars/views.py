
from django.shortcuts import render
from .models import Car
# Create your views here.
# created a function which will render the request
def index(request):
    new_cars = Car.objects.filter(category='New')[:6]
    used_cars = Car.objects.filter(category='Used')[:6]
    latest_cars= Car.objects.all().order_by('-date')[:5]

    context={
        'new_cars':new_cars,
        'used_cars':used_cars,
        'latest_cars':latest_cars
    }
    return render(request,'index.html', context)

