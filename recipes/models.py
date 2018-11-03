from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Recipe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    thumbnail = models.ImageField(upload_to='', default='no_image.png')
    description = models.TextField(max_length=300, null=True, blank=True)
    ingredients = models.TextField(max_length=1500, null=True)
    instructions = models.TextField(max_length=1800, null=True)
    cooking_time = models.PositiveIntegerField(default=0)
    servings = models.PositiveIntegerField(default=0)

    EASY = 'EASY'
    MODERATE = 'MODERATE'
    HARD = 'HARD'
    VERY_HARD = 'VERY HARD'
    DIFFICULTY_CHOICES = (
        (EASY, 'Easy'),
        (MODERATE, 'Moderate'),
        (HARD, 'Hard'),
        (VERY_HARD, 'Very Hard'),
    )
    difficulty = models.CharField(choices=DIFFICULTY_CHOICES, max_length=9, default=EASY)

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # automatically generates slug
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Recipe, self).save(*args, **kwargs)

    # instructions into step-by-step guide
    def methods_as_list(self):
        return self.instructions.split('\n')

    # ingredients into list
    def ingredients_as_list(self):
        return self.ingredients.split('\n')

    # converts time automatically to Hours & Minutes
    def get_time(self):
        time = int(str(self.cooking_time))
        time_hour, time_minutes = time // 60, time % 60
        cooking_time = ""
        if time_hour > 0:
            if time_hour == 1:
                cooking_time += "1 Hour"
            else:
                cooking_time += "%s Hours " % time_hour
        if time_minutes > 4:
            if len(cooking_time) > 0:
                cooking_time += ", "
            cooking_time += "%s Mins" % time_minutes
        return cooking_time

    def __str__(self):
        return self.title
