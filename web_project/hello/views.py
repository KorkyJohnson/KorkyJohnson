import re
from django.shortcuts       import render
from django.http            import HttpResponse
from django.utils.timezone  import datetime

# def home(request):
#     return HttpResponse("Hello, Django")

def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def hello_there(request, name):
    #
    # Old cod that handled the name/date data
    #
    # now = datetime.now()
    # formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # # Filter the name argument to letters only using regualr expressions. URL arguments
    # # can contain arbitary text, so we restrict to safe characters only.
    # match_object = re.match("[a-zA-Z]+", name)

    # if match_object:
    #     clean_name = match_object.group(0)
    # else:
    #     clean_name = "Friend"

    # content = "Hello there, " + clean_name + "! It's " + formatted_now
    # return HttpResponse(content)
    return render(
        request, 
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )