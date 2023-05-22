from django.shortcuts import render
from . import forms
# Create your views here.

def User(requset):
    form = forms.UserForm()

    if requset.method == 'POST':
        form = forms.UserForm(requset.POST)
    
        if form.is_valid():
            print('validation')
            form.save(commit=True)
            context = {'validation': form.cleaned_data}

            return render(requset, 'app2/user_form.html', context)

    context = {'user_form': form}
    return render(requset, 'app2/user_form.html', context)