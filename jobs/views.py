from django.shortcuts import render
from .models import Job, Project


# Create your views here.
def home(request):
    jobs = Job.objects.all()
    projects = Project.objects.all()
    return render(request, 'jobs/index.html',{'jobs':jobs, 'projects':projects})
    