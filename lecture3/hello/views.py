from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world!")

def ade(request):
    return HttpResponse("Hello, Ade!")

def brian(request):
    return HttpResponse("Hello, Brian!")


#def greet(request, name):
#    return HttpResponse(f"Hello {name.capitalize()}!")

# Hardcoding each user's name is bad habit but we can take advantage of django's ability dynamically figure out the name the user types in
 

# Let's return  a whole html page instead of just HttpResponse
# we will use render() for this
# render(request, "name of a template", {
#   context: optional and often used when you need to create a variable which html does not naturally allow
#   })

def index(request):
    return render(request, "hello/index.html") # this template was not created for us. so we have to create it:
# Step 1: inside the hello directory, create a new folder called templates
# Step 2: inside templates create a new folder called hello
# Step 3: inside hello, create a new file called index.html 
# Step 4: put in your html code into index. html



def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize() # create a new variable name and store the capitalised value of name inside it.
    })  # the template should have access to this variable
# We have separated our html file into a different file. 