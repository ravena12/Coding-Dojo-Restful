from django.shortcuts import render, redirect
import datetime
from .models import Products

from django.db.models import Count
from django.core.urlresolvers import reverse


def index(request):
	context = {
		"products": Products.objects.all()
	}
	return render(request, 'restfulTemp/index.html',context)

def new (request):
	return render(request, 'restfulTemp/new.html')

def create(request):
	Products.objects.create(name = request.POST['product_name'], description = request.POST['description'], price = request.POST['price'])
	return redirect('/new')

def show(request, id):
	context = {
		'person': Products.objects.get(id=id),
	}
	return render(request,'restfulTemp/show.html', context)


def edit(request, id):
	context = {
		'edit': Products.objects.get(id=id)
	}
	return render(request,'restfulTemp/edit.html', context)

def update(request, id):
	update = Products.objects.get(id = id)
	update.name = request.POST['product_name']
	update.description = request.POST['description']
	update.price = request.POST['price']
	update.save()
	return redirect('/')

def destroy(request, id):
	destroy = Products.objects.get(id=id).delete()
	return redirect('/')


