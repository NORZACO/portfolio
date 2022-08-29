from django.shortcuts import render, get_object_or_404
# import again
from bloge.models import Job



# Create your views here.
def homepage(request):
    betaleapp = Job.objects.all
    return render(request, 'bloge/index.html', {
        'betaleapp': betaleapp,
    })


def detailspage(request, job_id):
    job_details = get_object_or_404(Job, pk=job_id)
    return render(request, 'betaleapp/details.html', {
        'job' : job_details
    })