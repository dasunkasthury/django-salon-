from .models import Salon,Book,Freelancer,Timeslot,Job
#from django.template import loader
from django.shortcuts import render ,get_object_or_404
from django.http import Http404




def index(request):

    All_job = Job.objects.all()

    return render(request,'salon/index.html',{'All_job':All_job})