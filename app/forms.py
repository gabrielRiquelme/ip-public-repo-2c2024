from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
#|from django.contrib.auth.hashers import make_random_password


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        
        # Enviar correo con la contraseña
        subject = f'Bienvenido {user.username}'
        message = f'Hola {user.first_name} {user.last_name} te has registrado correctamente.\nQue disfrutes tu estadia en Rick & Morty.'
        from_email = 'gabrielcabj986@gmail.com'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)

        return user