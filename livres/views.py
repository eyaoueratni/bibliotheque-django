from django.shortcuts import get_object_or_404, redirect, render

from livres.forms import EmpruntForm, LivreForm
from livres.models import Album, Livre

# Create your views here.
def livres_disponibles(request):
    livres = Livre.objects.filter(disponible=True)
    return render(request, 'listeLivre.html', {'livres': livres})
def detail_livre(request,livre_id):
    livre=get_object_or_404(Livre,id=livre_id)
    return render(request, 'livredetail.html', {'livre': livre})

def ajouter_livre(request):
    if request.method == "POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("livres_disponibles")  # Redirige vers la liste des livres après ajout
    else:
        form = LivreForm()

    return render(request, "ajouter_livre.html", {"form": form})

def update_livre(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)
    if request.method == "POST":
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('livres_disponibles')
    else:
        form = LivreForm(instance=livre)
    return render(request, 'update_livre.html', {'form': form, 'livre': livre})

def emprunter_livre(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)
    if request.method == "POST":
        form = EmpruntForm(request.POST)
        if form.is_valid():
            emprunt = form.save(commit=False)
            emprunt.livre = livre
            emprunt.save()
            livre.disponible = False 
            livre.save()
            return redirect('livres_disponibles')
    else:
        form = EmpruntForm()
    return render(request, 'emprunter_livre.html', {'form': form, 'livre': livre})

def livres_non_disponibles(request):
    livres = Livre.objects.filter(disponible=False)
    return render(request, 'livres_non_disponibles.html', {'livres': livres})

def fct(request):
    res=Album.objects.all()
    return render(request,"index.html",{"res":res})

def total_livres_empruntes(request):
    livres = Livre.objects.all()  # Get all books to display them in the list
    total_empruntes = Livre.objects.filter(disponible=False).count()
    return render(request, 'listeLivre.html', {'livres': livres, 'total_empruntes': total_empruntes})
