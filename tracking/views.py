from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.forms import ModelForm
from django.utils import timezone

from .models import Farm, Unit, Level, Position, FlatForm
from .forms import FlatForm



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
		tag = request.POST['tray_tag']
		kind = request.POST['kind']
		var = request.POST['variety']
		vol = request.POST['seed_volume']
		sup = request.POST['supplier']
		ds = request.POST['date_seeded']
		du = request.POST['date_uncovered']
		dh = request.POST['date_harvested']
		current_level = Farm.objects.get(pk=farm_address).unit_set.get(pk=unit_id).level_set.get(pk=level_id)
		new_pos = Position(tray_tag=tag,
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
		context = {'position_data': position_data, 'tag':tag,'kind':kind,'var':var,'vol':vol,'sup':sup,'ds':ds,'du':du,'dh':dh,'current_level':current_level}
		return render(request, 'tracking/position.html',context)
	else:
		position_data = Farm.objects.get(pk=farm_address).unit_set.get(pk=unit_id).level_set.get(pk=level_id).position_set.all()
		context = {'position_data': position_data}
		return render(request, 'tracking/position.html', context)

def edit_flat(request, farm_address, unit_id, level_id, position_id):
	pos = Farm.objects.get(pk=farm_address).unit_set.get(pk=unit_id).level_set.get(pk=level_id).position_set.get(pk=position_id)
	form = FlatForm(instance=pos)
	context = {'form':form,
				'level':pos.level,
				'pos':pos,
				'tray_tag':pos.tray_tag,
				'kind':pos.kind,
				'variety':pos.variety,
				'seed_volume':pos.seed_volume,
				'supplier':pos.supplier,
				'date_seeded':pos.date_seeded,
				'date_uncovered':pos.date_uncovered,
				'date_harvested':pos.date_harvested}
	variables = RequestContext(request, context)
	if request.method == 'POST':
		form = FlatForm(request.POST, instance=pos)
		if form.is_valid():
			pos.tray_tag = form.cleaned_data['tray_tag']
			pos.kind = form.cleaned_data['kind']
			pos.variety = form.cleaned_data['variety']
			pos.seed_volume = form.cleaned_data['seed_volume']
			pos.supplier = form.cleaned_data['supplier']
			pos.date_seeded = form.cleaned_data['date_seeded']
			pos.date_uncovered = form.cleaned_data['date_uncovered']
			pos.date_harvested = form.cleaned_data['date_harvested']
			return render_to_response('tracking/position.html', variables)
	return render(request,'tracking/edit_flat.html',context)

def harvest_flat(request, farm_address, unit_id, level_id, position_id):
	# if request.method == 'POST':
	return render(request, 'tracking/harvest_flat.html')
# def insert_new_flat(request):
# 	if request.method == 'POST':
# 		new_flat = NewFlatForm(request.POST)
# 		if new_flat.is_valid():
# 			return HttpResponseRedirect('')
