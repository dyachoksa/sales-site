from django.views.generic import TemplateView, ListView

from blog.models import Post
from .models import Employee


class HomePage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["latest_posts"] = Post.objects.all()[:4]

        return context


class OurTeamView(ListView):
    model = Employee
