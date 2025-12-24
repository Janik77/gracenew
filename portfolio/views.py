from django.views.generic import DetailView, ListView

from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = "portfolio/projects_list.html"
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/project_detail.html"
    context_object_name = "project"
    slug_field = "slug"
    slug_url_kwarg = "slug"
