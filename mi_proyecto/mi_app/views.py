from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def inicio(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse(f'Bienvenido, {user.username}!')
        else:
            return render(request, 'index.html', {'error': 'Usuario o contraseña incorrectos'})

    return render(request, 'index.html')



from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Renderiza el template
