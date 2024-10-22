from django.contrib import admin
from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status")
    search_fields = ("name",)
    list_filter = ("status",)