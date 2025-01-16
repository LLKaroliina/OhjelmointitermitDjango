from django.shortcuts import render, redirect, get_object_or_404
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
    termit = Termit.objects.all()
    context = {'termit': termit}
    return render(request, 'termit.html', context)
def addtermit(request):
    a = request.POST['termi']
    b = request.POST['term']
    c = request.POST['selitys']
    Termit(termi = a, term = b, selitys = c).save()
    return redirect(request.META['HTTP_REFERER'])
# def termitview(request):
#     termit = Termit.objects.all()
#     context = {'termit': termit}
#     return render(request, 'termit.html', context)
# Create your views here.
