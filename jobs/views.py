from django.shortcuts import render
from .models import Job, Project, Resume


# Create your views here.
def home(request):
    jobs = Job.objects.all()
    projects = Project.objects.all()
    resume = Resume.objects.filter(pk=1).first()
    return render(request, 'jobs/index.html',
                    {'jobs':jobs, 'projects':projects, 'resume': resume})
