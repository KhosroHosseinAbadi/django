from django.views import generic
from django.urls import reverse_lazy

from . models import School


class SchoolListView(generic.ListView):
    model = School
    # template_name = "schools/school_list.html"
    # context_object_name = "school_list"


class SchoolDetailView(generic.DetailView):
    model = School
    # template_name = "schools/school_detail.html"
    # context_object_name = "school" OR "object"


class SchoolCreateView(generic.CreateView):
    model = School
    fields = "__all__"
    # template_name = "schools/school_form.html"
    # context_object_name = "form" AND "school" OR "object"


class SchoolUpdateView(generic.UpdateView):
    model = School
    fields = ("name", "principal")
    # template_name = "schools/school_form.html"
    # context_object_name = "form" AND "school" OR "object"


class SchoolDeleteView(generic.DeleteView):
    model = School
    success_url = reverse_lazy("schools:list_school")
    # template_name = "schools/school_confirm_delete.html"
    # context_object_name = "form" AND "school" OR "object"
