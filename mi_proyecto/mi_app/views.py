from django.shortcuts import render

def home(request):
    return render(request, 'mi_app/home.html')
