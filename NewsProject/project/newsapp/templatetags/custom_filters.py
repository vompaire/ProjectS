from django import template


register = template.Library()





@register.filter()
def currency(value):
   t = list(value.split())
   for i in range(len(t)):
      if t[i][0].istitle():
         t[i] = "*"
   t = " ".join(t)


   return f'{t}'