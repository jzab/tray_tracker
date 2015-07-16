from django.db import models
from django.utils import timezone
from django.forms import ModelForm
import datetime

class Farm(models.Model):
	farm_address = models.CharField(max_length=200, default=None)
	def __unicode__(self):
		return self.farm_address

class Unit(models.Model):
	farm = models.ForeignKey(Farm, null=True)
	unit_text = models.CharField(max_length=200, default = None) 
	unit_height = models.IntegerField(default=0)
	unit_length = models.IntegerField(default=0)
	pub_date = models.DateTimeField('Date')
	def __unicode__(self):
		return self.unit_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Level(models.Model):
	unit = models.ForeignKey(Unit, null=True)
	# farm = models.ForeignKey(Farm, null=True)
	level_rank = models.IntegerField(default=0)
	tray_slots = models.IntegerField(default=8)
	def __unicode__(self):
		return 'Level: ' + str(self.level_rank) + ' Trays: ' + str(self.tray_slots)

class Position(models.Model):
	position = models.IntegerField(default=0)
	tray_tag = models.CharField(max_length=10, default=None)
	kind = models.CharField(max_length=10, default=None)
	variety = models.CharField(max_length=10, default=None)
	seed_volume = models.IntegerField(default=0)
	supplier = models.CharField(max_length=10, default=None)
	date_seeded = models.DateTimeField('Date Seeded', null=True)
	date_uncovered = models.DateTimeField('Date Uncovered', null=True)
	date_harvested = models.DateTimeField('Date Harvested', null=True)
	level = models.ForeignKey(Level)

class FlatForm(ModelForm):
	class Meta:
		model = Position
		fields = ['position', 'tray_tag', 'kind', 'variety', 'seed_volume', 'supplier',
				'date_seeded', 'date_uncovered', 'date_harvested']
# class NewFlatForm(ModelForm):
# 	class Meta:
# 		model = Position
# 		fields = ['position', 'tray_tag', 'kind', 'variety', 'seed_volume', 'supplier',
# 				'date_seeded', 'date_uncovered', 'date_harvested']

