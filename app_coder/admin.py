from django.contrib import admin
from .models import Vtuber, User, Post, Moderator

# Register your models here.

admin.site.register(Vtuber)
admin.site.register(User)
admin.site.register(Moderator)
admin.site.register(Post)