from unicodedata import name
from django.contrib import admin
from .models import Person,Group

datpers="Aqui se añadiran los datos personales"
dated="Aqui se añadira la edad"

# Register your models here.


admin.site.register(Person)
admin.site.register(Group)
