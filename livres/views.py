from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework import viewsets
from livres.serializers import LivresSerializer, CategorySerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from livres.models import LivreModel, CategoryModel

User = get_user_model()


class LivresViewSet(viewsets.ModelViewSet):
    queryset = LivreModel.objects.all()
    serializer_class = LivresSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class LivresHome(ListView):
    model = LivreModel
    context_object_name = 'livres'
    template_name = "livres_list.html"


class LivresDetail(DetailView):
    model = LivreModel
    context_object_name = 'livre'
    template_name = "livres_detail.html"


class LivresCreate(CreateView):
    model = LivreModel
    template_name = "livres_create.html"
    fields = ['title', 'author', 'description', 'categories']


class LivresUpdate(UpdateView):
    model = LivreModel
    context_object_name = 'livre'
    template_name = "livres_update.html"
    fields = ['title', 'author', 'description', 'categories']


class LivresDelete(DeleteView):
    model = LivreModel
    context_object_name = 'livre'
    template_name = "livres_delete.html"
    success_url = reverse_lazy('livres:home')


class CategoriesMainView(ListView):
    model = CategoryModel
    context_object_name = 'categories'
    template_name = 'categories_list.html'


class CategoriesCreate(CreateView):
    model = CategoryModel
    template_name = 'categories_create.html'
    fields = ['nom']


def Livres_par_Categorie(request, nom_categorie):
    categorie = CategoryModel.objects.get(nom=nom_categorie)
    livres = LivreModel.objects.filter(categories=categorie)
    return render(request, 'livres_par_cat.html', {'livres': livres, 'category': categorie})


class CategoriesDelete(DeleteView):
    model = CategoryModel
    context_object_name = 'category'
    template_name = 'categories_delete.html'
    success_url = reverse_lazy('livres:home')
