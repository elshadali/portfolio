from django.shortcuts import render
from .models import Work

def work_list(request):
    work1 = Work.objects.all()[:3]
    work2 = Work.objects.all()[3:6]
    context = {
        'work1': work1,
        'work2': work2
    }
    return render(request, 'work/work.html', context)

def work_detail(request, work_slug):
    work = Work.objects.get(slug=work_slug)
    context = {
        'work': work
    }
    return render(request, 'work/work_detail.html', context)

