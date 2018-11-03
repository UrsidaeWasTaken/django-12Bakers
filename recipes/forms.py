from django.forms import ModelForm
from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'thumbnail',
            'description',
            'difficulty',
            'servings',
            'cooking_time',
            'ingredients',
            'instructions'
        ]

        labels = {
            'title': 'Recipe title',
            'thumbnail': 'Recipe image',
            'servings': 'Number of servings',
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'description'})
        self.fields['ingredients'].widget.attrs.update({'class': 'ingredients'})
        self.fields['instructions'].widget.attrs.update({'class': 'instructions'})
        self.fields['difficulty'].widget.attrs.update({'class': 'difficulty'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Give a short description of your recipe'})
        self.fields['ingredients'].widget.attrs.update({'placeholder': 'Separate each ingredient on a NEW line'})
        self.fields['instructions'].widget.attrs.update({'placeholder': 'Separate each instruction on a NEW line'})
