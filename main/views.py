from django.shortcuts import render
from job.models import Job
# Create your views here.

def index(request):
    jobs = Job.objects.all()[:8]
    context = {
        'jobpostings': jobs
    }
    return render(request, 'main/index.html', context)