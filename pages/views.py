from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .forms import ContactForm
from .models import Project, Message
from django.urls import reverse


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(CreateView, ContactForm):
    model = Message
    form_class = ContactForm
    template_name = "contact.html"


class ResumePageView(TemplateView):
    template_name = "resume.html"


class ProjectsListView(ListView):
    model = Project
    context_object_name = "project_list"
    template_name = "projects.html"
