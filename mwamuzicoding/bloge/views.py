
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    template_name = "bloge/index.html"
    context = {
        "name" : "WELCOME TO LINX SERVER"
    }
    #return HttpResponse("HELLO WORLD")
    return render(request, template_name, context)