from django.contrib import admin 
from django.urls import path 
from django.http import HttpResponse 
def home(request): 
    return HttpResponse("^<h1^>Job Autoposter Funciona^</h1^><p^>Tu aplicacion esta corriendo correctamente^</p^>") 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('', home), 
] 
