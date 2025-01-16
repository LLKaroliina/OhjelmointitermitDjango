from django.urls import include, path
from .views import landingview, termitview, addtermit
from . import views

urlpatterns = [
    #path('api/', include ('app')),
    #path('index/', landingview),
    path('', landingview),
    #TERMIT URL
    path('termit/', termitview),
    path('add-termit/', addtermit)
]