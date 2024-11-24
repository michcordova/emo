
from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm  # formulario para modelo de usuarios
from mainapp.forms import RegisterForm  # para importar las vistas que creamos en forms.py, en ves de usar lo de UserCreationForm
from django.contrib import messages
from django.contrib. auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  # quitar accesos a usuarios no loggeados
# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title':'Inicio',
        'content':'.::Bienvenido::.'
    })

def about(request):
    return render(request, 'mainapp/about.html', {
        'title':'Acerca de',
        'content':'.::Somos una::.'
    })

def mision(request):    
    return render(request, 'mainapp/mision.html', {
        'title':'Mision',
        'content':'.::Somos una::.'
    })

def vision(request):
    return render(request, 'mainapp/vision.html', {
        'title':'Vision'
    })
    
def incio_sesion(request):
    return render(request, 'mainapp/inicio_sesion.html', {
        'title': 'Inicio de Sesión',
    })
    
def inicio_sesion(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user=authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Bienvenido al inicio de sesión')
                return redirect('inicio')
            else:
                messages.warning(request, 'No es posible iniciar sesión')
        
        return render(request, 'user/inicio_sesion.html', {
            'title': 'Inicio de Sesión',
        })

def registro(request):
    if request.user.is_authenticated:
        redirect('inicio')
    else:
        register_form = RegisterForm()

        if request.method=="POST":
            register_form=RegisterForm(request.POST)

            if register_form.is_valid():  # verifica que los datos sea validos 
                register_form.save()  
                messages.success(request, "¡Registro éxitoso!")
                return redirect('inicio')


        return render(request, 'mainapp/registro.html', {
        'title': 'Registro de Usuario',
        'register_form': register_form

    })
        
        
    def cerrar_sesion(request):
        logout(request)
        return redirect('inicio')

# def error404(request, exception):
#     return redirect(request, 'inicio')

def error404_2(request, exception):
    return render(request, 'mainapp/404.html', status=404)