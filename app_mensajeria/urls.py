from django.urls import path
from app_mensajeria import views


urlpatterns = [
    path('enviar-mensaje/', views.enviar_mensaje, name = "enviar-mensaje" ),
    path('mostrar-mensajes/', views.mostrar_mensajes, name = "mostrar-mensajes" ),
    path('eliminar-mensaje/<int:id>', views.eliminar_mensajes, name = "eliminar-mensaje"),
    path('responder-mensaje/<int:id>/', views.responder_mensaje, name='responder-mensaje'),
    path('mensajes-enviados', views.mensajes_enviados, name='mensajes-enviados'),
]