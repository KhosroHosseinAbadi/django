from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from schools.models import School
from . models import Student
from . forms import AddStudentForm


class StudentDetailView(generic.DetailView):
    model = Student


class StudentCreateView(generic.CreateView):
    model = Student
    fields = "__all__"


class StudentUpdateView(generic.UpdateView):
    model = Student
    fields = "__all__"


class StudentDeleteView(generic.DeleteView):
    model = Student

    def get_success_url(self):

        return reverse_lazy("schools:detail_school", kwargs={"pk": self.object.school.pk})


def add_student_to_school(request, pk):
    form = AddStudentForm()

    if request.method == "POST":
        form = AddStudentForm(request.POST)

        if form.is_valid():
            school = School.objects.get(pk=pk)
            student = form.save(commit=False)
            student.school = school
            student.save()
            return HttpResponseRedirect(reverse("schools:detail_school", kwargs={"pk":pk}))

    return render(request, "students/add_student.html",{"form":form, "pk":pk})
