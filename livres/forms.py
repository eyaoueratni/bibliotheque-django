from django import forms

from livres.models import Livre ,Emprunt


class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ["titre", "auteur", "date_publication", "disponible"]

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['nom_emprunteur', 'date_emprunt']