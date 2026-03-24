from django.urls import path

from apps.estate.views import (
    home,
    about,
    PropertyView,
    PropertySingleView,
    AgentListView,
    AgentSingleView,
    ContactView,
)


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("properties/", PropertyView.as_view(), name="properties"),
    path(
        "properties/<slug:slug>/", PropertySingleView.as_view(), name="property-single"
    ),
    path("agents/", AgentListView.as_view(), name="agents"),
    path("agents/<slug:slug>/", AgentSingleView.as_view(), name="agent-single"),
    path("contact/", ContactView.as_view(), name="contact"),
]