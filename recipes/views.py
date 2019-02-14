from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from django.shortcuts import get_object_or_404
from .models import Recipe
from .forms import RecipeForm


class RecipeIndexView(ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'all_recipes'

    def get_object(self):
        return get_object_or_404(Recipe, slug=self.kwargs['slug'])


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


class RecipeCreate(CreateView):
    form_class = RecipeForm
    template_name = 'forms/recipes_form.html'

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('/login/')
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RecipeCreate, self).form_valid(form)

