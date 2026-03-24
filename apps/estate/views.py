from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from apps.estate.models import Estate, EstateAgent, EstateAgentComment
from apps.blog.models import Post
from apps.estate.forms import EstateAgentCommentForm


def home(request):
    estates = (
        Estate.objects.prefetch_related("images")
        .filter(is_featured=True)
        .order_by("-price")[:3]
    )
    properties = (
        Estate.objects.prefetch_related("images").all().order_by("-created_at")[:4]
    )
    agents = (
        EstateAgent.objects.select_related("avatar").order_by("-rating")[:3]
    )
    posts = (
        Post.objects.select_related("image").order_by("-created_at")[:4]
    )

    context = {
        "estates": estates,
        "properties": properties,
        "agents": agents,
        "posts": posts
    }
    return render(request, "estate/index.html", context=context)


def about(request):
    agents = (
        EstateAgent.objects.select_related("avatar").order_by("-rating")[:3]
    )
    return render(request, "about.html", context={"agents": agents})


class PropertyView(TemplateView):
    template_name = "estate/property-grid.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        limit, offset = self.request.GET.get("limit", 10), self.request.GET.get("offset", 0)
        pages_count = Estate.objects.count() // int(limit) + 1
        context["estates"] = Estate.objects.prefetch_related("images").order_by("-created_at")[int(offset) : int(offset) + int(limit)]
        context["limit"] = limit
        context["offset"] = offset
        context["pages_count"] = [i+1 for i in range(pages_count)]
        return context



class PropertySingleView(TemplateView):
    template_name = "estate/property-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["estate"] = Estate.objects.prefetch_related("images").get(slug=self.kwargs["slug"])
        context["form"] = EstateAgentCommentForm()
        return context


class EstateAgentCommentHandlerView(CreateView):
    model = EstateAgentComment
    form_class = EstateAgentCommentForm


class AgentListView(TemplateView):
    template_name = "agent-grid.html"


class AgentSingleView(TemplateView):
    template_name = "agent-single.html"


class ContactView(TemplateView):
    template_name = "contact.html"