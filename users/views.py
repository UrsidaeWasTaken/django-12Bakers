from django.contrib.auth.models import User
from django.views.generic import DetailView
from .models import Baker


class UserDetailView(DetailView):
    model = Baker
    slug_field = 'user__username'
    template_name = 'profiles/profile.html'
