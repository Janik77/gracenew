from django.views.generic import TemplateView

from core.views import LeadRequestCreateView


class HomeView(LeadRequestCreateView):
    template_name = "pages/home.html"
    success_url = "/?success=1"


class AboutView(TemplateView):
    template_name = "pages/about.html"


class ServicesView(TemplateView):
    template_name = "pages/services.html"


class ContactsView(LeadRequestCreateView):
    template_name = "pages/contacts.html"
