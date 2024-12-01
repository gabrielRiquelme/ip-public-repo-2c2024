from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
#|from django.contrib.auth.hashers import make_random_password
import random
import string

def generar_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = generar_password()
        user.save()

        # Enviar correo con la contraseña
        subject = 'Tu contraseña generada'
        message = f'Hola {user.first_name}, tu contraseña para {user.username} es: {user.password}'
        from_email = 'tu_email@example.com'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)

        return user