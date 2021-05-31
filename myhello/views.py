from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def myIndex(request):
    my_name=request.POST.get('name',"Hello...Heroku!!!")
    return HttpResponse("Hello "+my_name)