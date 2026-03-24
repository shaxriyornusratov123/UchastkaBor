from typing import Any

from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.blog.models import Post, PostComment


class BlogListView(TemplateView):
    template_name = "blog-grid.html"


class BlogSingleView(TemplateView):
    template_name = "blog-single.html"