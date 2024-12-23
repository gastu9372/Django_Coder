from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Post, Comentario
from .forms import PostForm, FormComentario
# Create your views here.

@login_required
def crear_post(request):    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.autor = request.user
            post.save()
            return redirect("mostrar-posts")
            #return redirect("detalles_post", id=crear_post.instance.id)
    else:
        form = PostForm()
    return render(request, "app_posts/forms/crear-o-editar.html", {"form":form})

def mostrar_posts(request):
    
    posts = Post.objects.all()
    
    return render(request, "app_posts/mostrar-posts.html", {"posts":posts})

def detalle_post(request, id):
    post = get_object_or_404(Post, id=id)
    posts = Post.objects.exclude(id=id)
    es_autor = post.autor == request.user # Se revisa si es el autor del post para logica de html
    es_admin = request.user.is_superuser # Se revisa si es admin para la logica de html
    
    # Logica para crear el comentario
    if request.method == "POST":
        comentario_form = FormComentario(request.POST, request.FILES)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            return redirect("detalle-post", id=id)
    else:
        comentario_form= FormComentario()
    
    comentarios = post.comentario.all
    return render(request, "app_posts/detalle-post.html", {"post":post, "posts": posts,"es_autor": es_autor, "es_admin": es_admin, "comentarios": comentarios, "comentario_form":comentario_form})

def editar_post(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if post.autor != request.user:
        return redirect('mostrar-posts')
    

    if request.method =="POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.editado = True
            form.save()
            return redirect("mostrar-posts")
    else:
        form=PostForm(instance=post)
    return render(request, "app_posts/forms/editar-post.html",{"form":form})

def eliminar_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("mostrar-posts")