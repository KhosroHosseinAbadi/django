from django.shortcuts import render

# Create your views here.
def app1_index(request):

    return render(request, 'app1/app1_index.html')

def app1_page1(request):
    
    context = {'page_message': 'This is page 1'}
    return render(request, 'app1/app1_page1.html', context)

def app1_page2(request):
    context = {'page_message': 'This IS PaGE 2'}
    return render(request, 'app1/app1_page2.html', context)
