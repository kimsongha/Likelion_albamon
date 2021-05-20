#데이터를 가공하는 곳
#redirect

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Alba
# Create your views here.

#main을 열어라
def main(request):
    albas = Alba.objects.all()
    context = {
        'albas' : albas
    }
    return render(request, 'main.html', context)

def detail(request, id):
    detail_data = get_object_or_404(Alba, pk=id)
    context = {
        'title' : detail_data.title, 
        'writer' : detail_data.writer, 
        'pub_date' : detail_data.pub_date, 
        'adress' : detail_data.adress, 
        'wage' : detail_data.wage, 
        'body' : detail_data.body, 
        'id' : id,
        'applicant' : detail_data.applicant,
    }
    return render(request, 'detail.html', context)

#create페이지를 띄우는 함수
def create_page(request):
    return render(request, 'create.html')

def create(request):
    new_data = Alba()
    new_data.title = request.POST['title']
    new_data.writer = request.POST['writer']
    new_data.adress = request.POST['adress']
    new_data.wage = request.POST['wage']
    new_data.body = request.POST['body']
    new_data.pub_date = timezone.now()
    new_data.save()
    return redirect('main')

def update_page(request, id):
    update_data = get_object_or_404(Alba, pk=id)
    context = {
        'id' : id,
        'title' : update_data.title, 
        'writer' : update_data.writer, 
        'adress' : update_data.adress, 
        'wage' : update_data.wage, 
        'body' : update_data.body, 
    }
    return render(request, 'update.html', context)

def update(request, id):
    update_data = get_object_or_404(Alba, pk=id)
    update_data.title = request.POST['title']
    update_data.writer = request.POST['writer']
    update_data.adress = request.POST['adress']
    update_data.wage = request.POST['wage']
    update_data.body = request.POST['body']
    update_data.pub_date = timezone.now()
    update_data.save()
    return redirect('main') 

def delete(request, id):
    delete_data = get_object_or_404(Alba, pk=id)
    delete_data.delete()
    return redirect('main')

