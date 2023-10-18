from django.shortcuts import render
from . models import Webpage, AccessRecord, Topic
# Create your views here.

def show_objects(request):
    entries = {
        'webpages': Webpage.objects.all(),
        'acc_recs': AccessRecord.objects.all(),
        'topics': Topic.objects.all(),
    }

    context = {'entries': entries}
    return render(request, 'app1/show_objects.html', context=context)