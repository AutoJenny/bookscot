from django.contrib import admin
from .models import Article, Directory, Role, Personnel
# Register your models here
admin.site.register(Article)
admin.site.register(Directory)
admin.site.register(Role)
admin.site.register(Personnel)