from django.contrib import admin

# Register your models here.

from livres.models import LivreModel, CategoryModel


class LivreModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'description']


class CategoriesModelAdmin(admin.ModelAdmin):
    list_display = ['nom']


admin.site.register(LivreModel, LivreModelAdmin)
admin.site.register(CategoryModel, CategoriesModelAdmin)
