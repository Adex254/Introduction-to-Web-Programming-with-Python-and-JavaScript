from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    hour = now.hour 
     
    if (7 <= hour < 12):
        greeting = "morning"
        theme = "morning-bg"

    elif (12 <= hour < 17):
        greeting = "afternoon" 
        theme = "afternoon-bg"
        
    else:
        greeting =  "evening"
        theme = "evening-bg"
        
             
    return render(request, "greeting/index.html", {
        
         "greeting": greeting,
         "hour": hour,
         "theme": theme
    })
        

           
def day(request):
    now = datetime.datetime.now()
    date = now.day

    if (date % 7) == 5:
        day = "monday"

    elif (date % 7) == 6:
        day = "tuesday"

    elif (date % 7) == 0:
        day = "wednesday"

    elif (date % 7) == 1:
        day = "thursday"

    elif (date % 7) == 2:
        day = "friday"

    elif (date % 7) == 3:
        day = "saturday"

    else:
        day = "sunday"

    return render(request, "greeting/day.html", {
        "day": day
        })