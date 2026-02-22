from django.test import TestCase

from livres.models import Livre

# Create your tests here.
class LivreTestCase(TestCase):
    def setUp(self):
        Livre.objects.create(titre="django unchained", auteur="tarantino",date_publication="2012-01-01")

    def test_liste_livres(self):
        response=self.client.get('/livres_disponibles/')
        self.assertEqual(response.status_code,200)    
    def test_ajouter_livre(self):
         # Envoi d'une requête POST pour ajouter un nouveau livre
        response = self.client.post('/ajouter_livre/', {
            'titre': 'Nouveau Livre',
            'auteur': 'Auteur Nouveau',
            'date_publication': '2024-11-01',
            'disponible': True,
        })
        
        self.assertEqual(Livre.objects.count(),2)