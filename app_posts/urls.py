from app_posts import views
from django.urls import path

urlpatterns =[
    path('', views.mostrar_posts, name="mostrar-posts"),
    path('crear_post/', views.crear_post, name="crear-post"),
    path('detalle_post/<int:id>', views.detalle_post, name="detalle-post"),
    path('editar_post/<int:pk>', views.editar_post, name="editar-post"),
    path('eliminar_post/<int:id>', views.eliminar_post, name="eliminar-post"),
]