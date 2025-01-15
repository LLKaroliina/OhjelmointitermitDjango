from django.shortcuts import render, get_object_or_404
from .models import Termit
# from django.http import HttpResponse
# from django.template import loader

# def app(request):
#      return HttpResponse("Hello world!")
# def app(request):
#    template = loader.get_template('index.html')
#    return HttpResponse(template.render())
    
def landingview(request):
    return render(request, 'landingpage.html')
def termitview(request):
    termit= Termit.objects.all()
    context = {'termit': termit}
    return render(request, 'termit.html', context)
# def termitview(request):
#     termit = Termit.objects.all()
#     context = {'termit': termit}
#     return render(request, 'termit.html', context)
# Create your views here.
