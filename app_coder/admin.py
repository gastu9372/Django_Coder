from django.contrib import admin
from .models import Vtuber, Usuario, Post, Moderator, Profile

# Register your models here.

admin.site.register(Vtuber)
admin.site.register(Usuario)
admin.site.register(Moderator)
admin.site.register(Post)
admin.site.register(Profile)