from rest_framework import serializers
from livres.models import *


class LivresSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False, read_only=True)
    class Meta:
        model = LivreModel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False, read_only=True)
    class Meta:
        model = CategoryModel
        fields = '__all__'
