# mesas/templatetags/mesas_extras.py

from django import template

register = template.Library()

@register.filter
def estado_color(value):
    colores = {
        'disponible': 'success',
        'ocupada': 'danger',
        'reservada': 'warning'
    }
    return colores.get(value, 'secondary')
