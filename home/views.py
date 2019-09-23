from django.shortcuts import render, HttpResponse
from .models import Article, Doctor, Hospital
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'home/home.html')


def blog(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 6)
    page = request.GET.get('page')
    article_list_filter = paginator.get_page(page)
    article_dict = {'article_list_filter': article_list_filter}
    return render(request, 'home\\blog.html', article_dict)


def blog_detail(request, slug):
    q = Article.objects.filter(slug__iexact=slug)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    return render(request, 'home/blog_detail.html', {'detail': q})


def doctor(request):
    dlist = Doctor.objects.all()
    paginator = Paginator(dlist, 6)
    page = request.GET.get('page')
    doctor_list_filter = paginator.get_page(page)
    return render(request, 'home\doctor.html', {'dlist': doctor_list_filter})


def doctor_detail(request, slug):
    q = Doctor.objects.filter(slug__iexact=slug)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    return render(request, 'home/doctor_detail.html', {'doctor_detail': q})


def hospital(request):
    hlist = Hospital.objects.all()
    paginator = Paginator(hlist, 6)
    page = request.GET.get('page')
    hospital_list_filter = paginator.get_page(page)
    return render(request, 'home\hospital.html', {'hlist': hospital_list_filter})


def hospital_detail(request, slug):
    q = Hospital.objects.filter(slug__iexact=slug)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    return render(request, 'home/hospital_detail.html', {'hospital_detail': q})