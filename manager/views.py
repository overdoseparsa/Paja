from django.shortcuts import render

from .models import Tarakonsh

def create_api(request , author): 
    context = {
        'tarakonsh':Tarakonsh.objects.get(author__username = author)
    }

    # create static urls 
    return render(
        request , 'base.html' , context=context
    )   
