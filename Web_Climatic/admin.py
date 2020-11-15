from django.contrib import admin
from .models import articulo_Cientifico
class ArtAdmin(admin.ModelAdmin):
    list_display=("titulo","url","estado","creacion")
    list_filter=("estado",)
    search_fields=["titulo","contenido"]
    prepopulated_fields={"url":('titulo',)}

admin.site.register(articulo_Cientifico,ArtAdmin)