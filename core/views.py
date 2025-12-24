from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import LeadRequest


class LeadRequestCreateView(CreateView):
    model = LeadRequest
    fields = ["name", "phone", "message", "page"]
    template_name = "pages/contacts.html"
    success_url = reverse_lazy("pages:contacts")
