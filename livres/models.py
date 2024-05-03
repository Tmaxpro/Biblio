from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

User = get_user_model()


class CategoryModel(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['nom']
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('livres:home')


class LivreModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titre')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug')
    author = models.CharField(max_length=100, verbose_name='Auteur')
    description = models.TextField(verbose_name='Description')
    categories = models.ManyToManyField(CategoryModel, verbose_name='Categorie', related_name='livres')

    class Meta:
        ordering = ['title']
        verbose_name = 'Livre'
        verbose_name_plural = 'Livres'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            total = self.title + '' + self.author
            self.slug = slugify(total)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('livres:home')
