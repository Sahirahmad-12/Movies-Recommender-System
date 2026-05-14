from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome Sahil! Django is running successfully 🎉")
