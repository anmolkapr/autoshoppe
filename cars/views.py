from django.shortcuts import render

# Create your views here.
# created a function which will render the request
def index(request):
    return render(request,'index.html')
