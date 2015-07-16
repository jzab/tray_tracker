from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.forms import ModelForm

from .models import Farm, Unit, Level, Position, FlatForm



def index(request):
	farm_list = Farm.objects.order_by('-farm_address')
	context = {'farm_list': farm_list,}
	return render(request, 'tracking/index.html', context)

def detail(request, farm_address):
	tallest_unit_list = Farm.objects.get(pk=farm_address).unit_set.all()
	context = {'tallest_unit_list': tallest_unit_list}
	return render(request, 'tracking/detail.html', context)
	# return HttpResponse("You're looking at the farm located at: %s." % Farm.objects.get(pk=farm_address))

def levels(request, farm_address, unit_id):
	level_list = Farm.objects.get(pk=farm_address).unit_set.get(pk=unit_id).level_set.order_by('-level_rank')
	context = {'level_list': level_list}
	return render(request, 'tracking/levels.html', context)
	# return HttpResponse("You're looking at the levels of Unit: %s, located at: %s." % (Farm.objects.get(pk=farm_address).unit_set.get(pk=unit_id), Farm.objects.get(pk=farm_address)))

def positions(request, farm_address, unit_id, level_id):
	position_data = Farm.objects.get(pk=farm_address).unit_set.get(pk=unit_id).level_set.get(pk=level_id).position_set.all()
	context = {'position_data': position_data}
	return render(request, 'tracking/position.html', context)

def add_flat(request):
	if request.method == 'POST':
		form = FlatForm(None)
		if form.is_valid():
			print "Hello"
			form.save()
			return render(request, 'tracking/position.html')
	else:
		form = FlatForm()
	return render_to_response('tracking/insert_flat.html', {'form': form})

def edit_flat(request, farm_address, unit_id, level_id, position_id):
	if request.method == 'POST':
		form = FlatForm(request.POST, Farm.objects.get(pk=farm_address).unit_set.get(pk=unit_id).level_set.get(pk=level_id).position_set.get(pk=position_id))
		if form.is_valid():
			print "Hello World"
			form.save()
			return HttpResponseRedirect('tracking/{{ farm_address }}/{{ unit_id }}/{{ level_id }}')
		else:
			return render_to_response('tracking/edit_flat.html', {'form': form})
# def insert_new_flat(request):
# 	if request.method == 'POST':
# 		new_flat = NewFlatForm(request.POST)
# 		if new_flat.is_valid():
# 			return HttpResponseRedirect('')
