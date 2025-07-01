from django.http import HttpResponse

def home(request):
    return HttpResponse("Добро пожаловать в мой блог!")
# Create your views here.
