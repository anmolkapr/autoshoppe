
from django.shortcuts import render,get_object_or_404
from .models import Car
from .filters import CarFilter
# Create your views here.
# created a function which will render the request
def index(request):
    new_cars = Car.objects.filter(category='New')[:6]
    used_cars = Car.objects.filter(category='Used')[:6]
    latest_cars= Car.objects.all().order_by('-date')[:5]
    all=Car.objects.all()
    myFilter=CarFilter(request.GET,queryset=all)
    all=myFilter.qs

    context={
        'new_cars':new_cars,
        'used_cars':used_cars,
        'latest_cars':latest_cars,
        'all':all,
        'myFilter':myFilter        
    }
    return render(request,'index.html', context)

def filter_results(request):
    all=Car.objects.all()
    myFilter=CarFilter(request.GET,queryset=all)
    all=myFilter.qs
        
    context = {
        'all': all,
        'myFilter':myFilter
    }

    return render(request,"filter_results.html",context)

def car_detail(request, car_id):
    cars = get_object_or_404(Car,id = car_id)
    context = {
        'cars': cars
    }
    return render(request,"car_detail.html",context)
