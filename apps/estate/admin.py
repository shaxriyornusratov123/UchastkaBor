from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.estate.models import (
    Amenities,
    Estate,
    EstateAgent,
    EstateAgentComment,
    EstateCategory,
)


@admin.action(description="Mark selected Estates as featured")
def mark_as_featured(modeladmin, request, queryset):
    queryset.update(is_featured=True)


@admin.action(description="Mark selected Estates as unfeatured")
def mark_as_unfeatured(modeladmin, request, queryset):
    queryset.update(is_featured=False)


@admin.register(EstateAgent)
class EstateAgentAdmin(ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "phone",
        "email",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "email",
        "phone",
    ]
    fields = [
        "first_name",
        "last_name",
        "bio",
        "avatar",
        "phone",
        "mobile",
        "email",
        "telegram",
        "whatsapp",
        "instagram",
        "facebook",
        "x",
    ]


@admin.register(EstateCategory)
class EstateCategoryAdmin(ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    search_fields = [
        "name",
    ]
    fields = [
        "name",
    ]


@admin.register(Amenities)
class AmenitiesAdmin(ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    search_fields = [
        "name",
    ]
    fields = [
        "name",
    ]


@admin.register(Estate)
class EstateAdmin(ModelAdmin):
    list_display = [
        "id",
        "name",
        "agent",
        "category",
        "state",
        "region",
        "status",
        "price",
        "currency",
    ]
    list_filter = [
        "status",
        "category",
        "state",
        "region",
        "currency",
    ]
    search_fields = [
        "name",
        "address",
    ]
    filter_horizontal = [
        "amenities",
        "images",
    ]
    actions = [mark_as_featured, mark_as_unfeatured]


@admin.register(EstateAgentComment)
class EstateAgentCommentAdmin(ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
    ]
    search_fields = [
        "name",
        "email",
    ]
    fields = [
        "name",
        "email",
        "comment",
    ]