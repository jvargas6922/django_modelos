from django.contrib import admin
from .models import Persona

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name','email', 'age']

admin.site.register(Persona, PersonaAdmin)
#admin.site.register(Persona)
