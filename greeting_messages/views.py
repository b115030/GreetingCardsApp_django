from django.shortcuts import render
from .models import Greetings
from django.views import View
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

def get(request):
    post = Greetings.objects.all()
    return render(request, 'greeting_messages/index.html', {'myjson': post})

class GreetingView(View):
    def get(self, request):

        post = Greetings.objects.all()
        print(post)
        data = serializers.serialize('json', post)
        return HttpResponse(data)