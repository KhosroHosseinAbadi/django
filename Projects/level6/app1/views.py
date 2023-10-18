from django.shortcuts import render
from . forms import AddStudentForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from . models import School, Student
# Create your views here.


class SchoolListView(ListView):
    model = School
    # template_name = 'app1/school_list.html'    # this is default
    # context_object_name = 'school_list'        # this is default


class SchoolDetailView(DetailView):
    model = School
    # template_name = 'app1/school_detail.html'          # this is default
    # context_object_name = 'school' OR 'object'         # this is default


class SchoolCreateView(CreateView):
    model = School
    fields = '__all__'
    # template_name = 'app1/school_form.html'                  # this is default
    # context_object_name = 'form' AND 'school' OR 'object'    # this is default



class SchoolUpdateView(UpdateView):
    model = School
    fields = ('name', 'principal')
    # template_name = 'app1/school_form.html'                  # this is default
    # context_object_name = 'form' AND 'school' OR 'object'    # this is default


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('app1:school_list')
    # template_name = 'app1/school_confirm_delete.html'        # this is default
    # context_object_name = 'form' AND 'school' OR 'object'    # this is default


#------------------------------------------------------------
# Students Views --------------------------------------------

class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'


class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'


class StudentDeleteView(DeleteView):
    model = Student

    def get_success_url(self):

        return reverse_lazy('app1:school_detail', kwargs={'pk': self.object.school.pk})
    

def add_student_to_school(request, pk):
    form = AddStudentForm()

    if request.method == 'POST':
        form = AddStudentForm(request.POST)

        if form.is_valid():
            school = School.objects.get(pk=pk)
            student = form.save(commit=False)
            student.school = school
            student.save()
            return HttpResponseRedirect(reverse('app1:school_detail', kwargs={'pk':pk}))

    return render(request, 'app1/add_student.html',{'form':form, 'pk':pk})
    
    
