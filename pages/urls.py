from django.urls import path

from core.views import LeadRequestCreateView
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("services/", views.ServicesView.as_view(), name="services"),
    path("contacts/", LeadRequestCreateView.as_view(), name="contacts"),
]
