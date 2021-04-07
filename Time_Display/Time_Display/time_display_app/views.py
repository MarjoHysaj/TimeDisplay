from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context={
        "time": strftime("%d-%m-%Y %I:%M %p %a ", gmtime())
    }
    return render(request, "index.html", context)
