from django.contrib import admin
from .models import Category, ViewCount

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'description', 'slug', 'views', 'parent')
    search_fields = ('name', 'title', 'slug')
    list_filter = ('parent',)
    autocomplete_fields = ('parent',)
    prepopulated_fields = {"slug": ("name",)} #Esto lo que hace es que cuando estas escribiendo el nombre de la categoria en el admin, se llena automaticamente el slug
    readonly_fields = ('views',)

class ViewCountAdmin(admin.ModelAdmin):
    list_display = ('category', 'ip_address')
    search_fields = ('category__name', 'ip_address')

admin.site.register(Category, CategoryAdmin)
admin.site.register(ViewCount, ViewCountAdmin)