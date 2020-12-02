from django.shortcuts import render
from .models import Greetings
from django.views import View
from django.core import serializers
from django.http import HttpResponse
import json

# Create your views here.

def get_data_from_backend(request):
    '''
    gets the data from backend into an array
    :return: post_array to greeting_messages/index.html
    '''
    post = Greetings.objects.all()
    return render(request, 'greeting_messages/index.html', {'post_array': post})

class GreetingView(View):
    def get(self, request):

        post = Greetings.objects.all()
        data = list(post.values('name','message'))
      
        return HttpResponse(json.dumps(data))
        # data = serializers.serialize('json', post)
        # return HttpResponse(data)