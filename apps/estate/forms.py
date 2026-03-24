from django import forms
from django.forms import ModelForm, Form

from apps.estate.models import EstateAgentComment


class EstateAgentCommentForm(ModelForm):
    class Meta:
        model = EstateAgentComment
        fields = ["name", "email", "comment", "stars_count"]

