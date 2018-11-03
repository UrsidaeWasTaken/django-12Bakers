from django.contrib import admin
from .models import Recipe


# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(Recipe, RecipeAdmin)
