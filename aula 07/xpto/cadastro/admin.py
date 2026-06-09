from django.contrib import admin

# Register your models here.
from .models import Cliente
admin.site.register(Cliente)
from .models import Curso
admin.site.register(Curso)