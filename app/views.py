# capa de vista/presentación
from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from app.forms import RegisterForm
from django.contrib import messages

#from django.contrib.auth.hashers import make_random_password



def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):
    images = [] 
    images = services.getAllImages() # -- LISTA CON LAS CARD YA CARGADAS 
    paginas = Paginator(images,6) # -- PAGINAR ARTICULOS 6 por pag.

    #-- Seteo numero de paginas.
    page = request.GET.get('page')
    page_cards = paginas.get_page(page)

    favourite_list = []

    return render(request, 'home.html', { 'images': page_cards, 'favourite_list': favourite_list })

def search(request):
    search_msg = request.POST.get('query', '')

    # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py,
    # y luego renderiza el template (similar a home).
    if (search_msg != ''):
        pass
    else:
        return redirect('home')
    

def register_pag(request):
    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Tu Usuario fue creado correctamente, se envio tu credencial de acceso a tu email.')
            
            return redirect('login')

    return render(request,'registration/registro.html',{
        'Titulo':'Registrate aqui',
        'register_form':register_form
    })

def login_pag(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return render(request, 'login.html')



    return render(request,'registration/login.html',{
        'title':'Inicia sesion'
    })


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        # Maneja el caso de una solicitud GET (opcional)
        return redirect('login')  # O render una página de confirmación


# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass