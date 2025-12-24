from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LeadRequestForm
from .models import LeadRequest


class LeadRequestCreateView(CreateView):
    model = LeadRequest
    form_class = LeadRequestForm
    success_url = reverse_lazy("pages:contacts")

    def form_valid(self, form):
        form.instance.page = self.request.path
        return super().form_valid(form)

    def get_success_url(self):
        return f"{self.success_url}?success=1"
