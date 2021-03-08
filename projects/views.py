from django.shortcuts import render
from .models import Project

# Create your views here.

def project_list_view(request):
    projectlist = Project.objects.all()
    return render(request,'index.html',context={'projects':projectlist})

def project_detail_view(request, pk):
    data = Project.objects.get(pk=pk)
    return render(request,'project_detail.html',context={'project':data})