from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('livres_disponibles/', views.livres_disponibles, name='livres_disponibles'),
    path('ajouter_livre/', views.ajouter_livre, name='ajouter_livre'),
    path("livre/<int:livre_id>/", views.detail_livre, name="detail_livre"),
    path('livre/<int:livre_id>/modifier/', views.update_livre, name='update_livre'),
    path('livre/<int:livre_id>/emprunter/', views.emprunter_livre, name='emprunter_livre'),
    path('livre/non-disponibles/', views.livres_non_disponibles, name='livres_non_disponibles'),
    path('image/', views.fct, name='image'),
    path('countEmprunt/', views.total_livres_empruntes, name='count_emprunt'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)