from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from livres.views import *
from rest_framework.routers import DefaultRouter


app_name = 'livres'

router = DefaultRouter()
router.register(r'livres', LivresViewSet, basename='livres')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', LivresHome.as_view(), name='home'),
    path('livres/ajouter/', LivresCreate.as_view(), name='create_livre'),
    path('livres/modifier/<str:slug>/', LivresUpdate.as_view(), name='update_livre'),
    path('livres/supprimer/<str:slug>/', LivresDelete.as_view(), name='delete_livre'),
    path('livres/<str:slug>/', LivresDetail.as_view(), name='detail_livre'),
    path('categories/', CategoriesMainView.as_view(), name='categories'),
    path('categories/ajouter/', CategoriesCreate.as_view(), name='create_categories'),
    path('categories/livres/<str:nom_categorie>/', Livres_par_Categorie, name='livres_par_categories'),
]