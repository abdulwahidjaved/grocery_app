from django.http import HttpResponse


def index(request):
    return HttpResponse(("Hello Abdul"))

def home(request):
    return HttpResponse("This is home")

def features(request):
    return HttpResponse("This is Features Page")

def about(request):
    return HttpResponse("This is About Page")

def contact(request):
    return HttpResponse("This is Contact Page")