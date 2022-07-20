"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        # path('', views.index, name='index'),
        # path('Propietario/<int:id>', views.obtener_Propietario,
        #     name='obtener_Propietario'),
        # path('crear/Propietario', views.crear_Propietario,
        #     name='crear_Propietario'),
        # path('editar_Propietario/<int:id>', views.editar_Propietario,
        #     name='editar_Propietario'),
        # path('eliminar/Propietario/<int:id>', views.eliminar_Propietario,
        #     name='eliminar_Propietario'),
        # # numeros telefonicos
        # path('crear/numero/telefonico', views.crear_numero_telefonico,
        #     name='crear_numero_telefonico'),
        # path('editar/numero/telefonico/<int:id>', views.editar_numero_telefonico,
        #     name='editar_numero_telefonico'),
        # path('crear/numero/telefonico/Propietario/<int:id>',
        #     views.crear_numero_telefonico_Propietario,
        #     name='crear_numero_telefonico_Propietario'),
        # path('saliendo/logout/', views.logout_view, name="logout_view"),
        # path('entrando/login/', views.ingreso, name="login"),
 ]
