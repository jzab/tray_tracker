from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.forms import ModelForm
from django.utils import timezone

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
	if request.method == 'POST':
		pos = request.POST['position']
		kind = request.POST['kind']
		var = request.POST['variety']
		vol = request.POST['seed_volume']
		sup = request.POST['supplier']
		ds = request.POST['date_seeded']
		du = request.POST['date_uncovered']
		dh = request.POST['date_harvested']
		new_pos = Position(id=1,
							tray_tag=pos,
							kind=kind,
							variety=var,
							seed_volume=vol,
							supplier=sup,
							date_seeded=ds,
							date_uncovered=du,
							date_harvested=dh,
							level=Farm.objects.get(pk=farm_address).unit_set.get(pk=unit_id).level_set.get(pk=level_id))
		new_pos.save()
		position_data = Farm.objects.get(pk=farm_address).unit_set.get(pk=unit_id).level_set.get(pk=level_id).position_set.all()
		context = {'position_data': position_data}
		return render(request, 'tracking/position.html',context)
	else:
		position_data = Farm.objects.get(pk=farm_address).unit_set.get(pk=unit_id).level_set.get(pk=level_id).position_set.all()
		context = {'position_data': position_data}
		return render(request, 'tracking/position.html', context)

def edit_flat(request, farm_address, unit_id, level_id, position_id):
	if request.method == 'POST':
		return render(request, 'tracking/edit_flat.html')

def harvest_flat(request, farm_address, unit_id, level_id, position_id):
	# if request.method == 'POST':
	return render(request, 'tracking/harvest_flat.html')
# def insert_new_flat(request):
# 	if request.method == 'POST':
# 		new_flat = NewFlatForm(request.POST)
# 		if new_flat.is_valid():
# 			return HttpResponseRedirect('')
