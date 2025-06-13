from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Configura los grupos y el usuario gerente inicial'

    def handle(self, *args, **kwargs):
        # Crear grupos
        gerentes, _ = Group.objects.get_or_create(name='Gerentes')
        cajeros, _ = Group.objects.get_or_create(name='Cajeros')

        # Crear usuario gerente si no existe
        if not User.objects.filter(username='gerente').exists():
            gerente = User.objects.create(
                username='gerente',
                password=make_password('gerente123'),
                is_staff=True
            )
            gerente.groups.add(gerentes)
            self.stdout.write(self.style.SUCCESS('Usuario gerente creado exitosamente'))
        else:
            self.stdout.write(self.style.SUCCESS('El usuario gerente ya existe'))

        self.stdout.write(self.style.SUCCESS('Configuración completada')) 