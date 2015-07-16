## forms.py ##

from django.forms import ModelForm
from .models import Position

class FlatForm(ModelForm):
	class Meta:
		model = Position
		fields = ['position', 'tray_tag', 'kind', 'variety', 'seed_volume', 'supplier',
				'date_seeded', 'date_uncovered', 'date_harvested']
