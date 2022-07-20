from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Propietario, Departamento

# Agregar la clase Propietario para administrar desde
# interfaz de administración
# admin.site.register(Propietario)

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Propietario

    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 

# admin.site.register se lo altera
# el primer argumento es el modelo (Propietario)
# el segundo argumento la clase PropietarioAdmin
admin.site.register(Propietario)

# Agregar la clase Departamento para administrar desde
# interfaz de administración
# admin.site.register(Departamento)

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Departamento


admin.site.register(Departamento)
