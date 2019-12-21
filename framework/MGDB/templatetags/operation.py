from django import template

register = template.Library()

@register.filter
def modulo(num, val):
  return num % val

@register.filter
def modulo_plusone(num, val):
  if (num + 1) % val == 0:
    return True
  else:
    return False