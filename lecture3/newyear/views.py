from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.day == 1 and now.month== 1  # I want the template newyear/index.html to have access to the value of the variable "newyear" (returns True or False)
    })