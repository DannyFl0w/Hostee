from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Crea un usuario con un rol específico'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Nombre de usuario')
        parser.add_argument('password', type=str, help='Contraseña')
        parser.add_argument('rol', type=str, choices=['gerente', 'cajero'], help='Rol del usuario (gerente o cajero)')
        parser.add_argument('--staff', action='store_true', help='El usuario es staff')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        rol = kwargs['rol']
        is_staff = kwargs['staff']

        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR(f'El usuario {username} ya existe'))
            return

        # Crear el usuario
        user = User.objects.create(
            username=username,
            password=make_password(password),
            is_staff=is_staff
        )

        # Asignar el grupo
        grupo_nombre = 'Gerentes' if rol == 'gerente' else 'Cajeros'
        grupo, _ = Group.objects.get_or_create(name=grupo_nombre)
        user.groups.add(grupo)

        self.stdout.write(self.style.SUCCESS(f'Usuario {username} creado exitosamente como {grupo_nombre}')) 