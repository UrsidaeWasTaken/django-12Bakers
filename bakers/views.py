from .forms import RegistrationForm
from django.urls import reverse_lazy
from django.views import generic


class Registration(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'
