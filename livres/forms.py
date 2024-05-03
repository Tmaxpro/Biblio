from django import forms
from livres.models import LivreModel, CategoryModel


class LivresForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=CategoryModel.objects.all(),
                                                widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = LivreModel
        fields = ['title', 'author', 'description', 'categories']
