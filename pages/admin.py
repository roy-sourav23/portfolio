from django.contrib import admin
from .models import Project, Message


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "codeLink", "demo")


class MessageAdmin(admin.ModelAdmin):
    list_display = ("fname", "lname", "email", "phone", "message")


admin.site.register(Project, ProjectAdmin)

admin.site.register(Message, MessageAdmin)
