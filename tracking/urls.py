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
		url(r'^(?P<farm_address>[0-9]+)/(?P<unit_id>[0-9]+)/(?P<level_id>[0-9]+)/$', views.positions, name='positions')]