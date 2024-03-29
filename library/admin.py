from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    # Adiciona slugs automatico
    prepopulated_fields = {
        'slug': ('title',)
    }
    
class GenreAdmin(admin.ModelAdmin):
    # Adiciona slugs automatico
    prepopulated_fields = {
        'slug': ('name',)
    }

class LanguageAdmin(admin.ModelAdmin):
    # Adiciona slugs automatico
    prepopulated_fields = {
        'slug': ('name',)
    }
    

admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Language, LanguageAdmin)



# # Exibe informações adicionais

# list_display = [
#     'id',
#     'title',
#     'created_at',
#     'is_published',
#     'author'
# ]

# # Adiciona links as visualizações

# list_display_links = [
#     'title',
#     'created_at'
# ]

# # Adiciona metodos de busca

# search_fields = [
#     'id',
#     'title',
#     'description',
#     'created_at',
#     'slug'
# ]

# # Adiciona metodo de filtro 

# list_filter = [
#     'category',
#     'author',
#     'is_published',
#     'preparation_steps_is_html'
# ]
    
# # Configura quantos itens por página serão exibidos na tabela ADMIN

# list_per_page = 10

# list_editable = [
#     'is_published'
# ]

# # Organiza como as informações são listadas por id

# ordering = [
#     '-id'
# ]


