from django.contrib import admin
from .models import Album, Livre, Emprunt
# Register your models here.
# Personnalisation du modèle Livre dans l'administration
@admin.register(Emprunt)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(Livre)
class AuthorAdmin(admin.ModelAdmin):
    list_display=("titre","auteur")
admin.site.register(Album)