from django.conf.urls import url
from .models import Farm, Unit, Level, Position
from . import views

urlpatterns = [
		# ex: /tracking/
		url(r'^$', views.index, name='index'),
		# ex: /tracking/5
		url(r'^(?P<farm_address>[0-9]+)/$', views.detail, name='detail'),
		# ex: /tracking/5/levels/
		url(r'^(?P<farm_address>[0-9]+)/(?P<unit_id>[0-9]+)/$', views.levels, name='levels'),
		# ex: /tracking/5/levels/slots
		url(r'^(?P<farm_address>[0-9]+)/(?P<unit_id>[0-9]+)/(?P<level_id>[0-9]+)/$', views.positions, name='positions'),
		# ex: add a flat to the database
		# url(r'^(?P<farm_address>[0-9]+)/(?P<unit_id>[0-9]+)/(?P<level_id>[0-9]+)/add_flat/$', views.add_flat, name='positions'),
		# ex: user clicks on edit button next to a flat
		url(r'^(?P<farm_address>[0-9]+)/(?P<unit_id>[0-9]+)/(?P<level_id>[0-9]+)/(?P<position_id>[0-9]+)/edit_flat/$', views.edit_flat, name='edit_flat'),
		# ex: user clicks on harvest button next to a flat
		url(r'^(?P<farm_address>[0-9]+)/(?P<unit_id>[0-9]+)/(?P<level_id>[0-9]+)/(?P<position_id>[0-9]+)/harvest_flat/$', views.harvest_flat, name='harvest_flat'),
		url(r'^(?P<farm_address>[0-9]+)/(?P<unit_id>[0-9]+)/(?P<level_id>[0-9]+)/edited/$', views.edited, name='edited'),
		]