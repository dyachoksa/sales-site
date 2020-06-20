from django.views.generic import ListView

from blog.models import Post


class BlogIndexView(ListView):
    queryset = Post.objects.select_related("category").order_by("-pk").all()
    context_object_name = "posts"
