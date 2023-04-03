from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    ResumePageView,
    ProjectsListView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("resume/", ResumePageView.as_view(), name="resume"),
    path("projects/", ProjectsListView.as_view(), name="projects"),
]
