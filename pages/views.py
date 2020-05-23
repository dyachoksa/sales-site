from django.views.generic import TemplateView, ListView

from .models import Employee


class HomePage(TemplateView):
    template_name = "index.html"


class OurTeamView(ListView):
    model = Employee
