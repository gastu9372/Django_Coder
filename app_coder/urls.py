from app_coder import views
from django.urls import path

# Es buena practica escribir todas las funciones 1x1, buena practica lo explicito
urlpatterns = [
    path('inicio/', views.index, name="Inicio"),
    path('vtubers/', views.vtubers, name ="Vtubers"),
    path('mods/', views.mods, name="Mods"),
    path('users/', views.users, name="Users"),
    path('posts/', views.posts, name="Posts"),
    path('formulario/', views.formulario_vtuber_api, name="Formulario"),
    path('del_vtuber/<int:id>', views.eliminar_vtuber, name="Eliminar"),
    path('edit_vtuber/<int:id>', views.editar_vtuber, name="Editar"),
    
    # Sesiones
    path("login/", views.login_view, name = "Login" ),
    path("logout/", views.user_logout, name = "Logout" ),
    path("register/", views.register_view, name = "Register" ),
    
]
