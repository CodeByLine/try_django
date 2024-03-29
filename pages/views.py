from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


# def home_view(args, **kwargs):

#     return "<h1>Hello World</h1>"

def home_view(request):
    print(request.user)
    my_context = {
        "my_dog": "Coco",
        "my_hunter" : "Pumpkin",
        "my_praying_mantis" : "Tiny",
        "my_buddies" : ["Coco", "Pumpkin", "Tiny"],
        "my_html" : "<h2>Safe filter</h2>",
    }

    return render(request, 'home.html', my_context)


    # html = "<html><body><h1>Hello World</h1></body></html>"
    # return HttpResponse(html)


def another_view(request, *args, **kwargs):
    print(args, kwargs) 
    html = "<html><body><h1>Hello World</h1><br><h2>View <span style='color:red'> Terminal </span> for the print out statement of args and kwargs</h2></body></html>"
    return HttpResponse(html)

def also_view(request, *args, **kwargs):
    print(args, kwargs)
    # print(request.user)
    html = "<html><body><h1>Hello World</h1><br><h2>View <span style='color:red'> Terminal </span> for the print out statement of args and kwargs</h2></body></html>"
    return render(request, 'home.html', {})