from django.contrib import admin
from .models import DataSet, Template, Script, Directory

@admin.register(DataSet)
class DataSetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Customize as needed
@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Customize as needed
admin.site.register(Script)
admin.site.register(Directory)
