from django.shortcuts import render
from .models import Greetings

# Create your views here.

def get(request):
    post = Greetings.objects.all()
    return render(request, 'greeting_messages/index.html', {'mydata_json': post})