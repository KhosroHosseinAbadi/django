from django.shortcuts import render
from . import forms
# Create your views here.

def comment_form_view(request):
    form = forms.CommentForm()

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)

        if form.is_valid():
            context = {'valid_comment_form': form.cleaned_data}

            return render(request, 'app1/comment_form.html', context)
    
    
    context = {'comment_form': form}
    return render(request, 'app1/comment_form.html', context)


