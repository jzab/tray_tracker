from django.contrib import admin

from .models import Farm, Unit, Level, Position

class PositionInline(admin.TabularInline):
	model = Position
	extra = 0
	fieldsets = [('Position', {'fields': ['tray_tag','kind','variety','seed_volume','supplier',
				'date_seeded','date_uncovered','date_harvested']})]

class LevelAdmin(admin.ModelAdmin):
	fieldsets = [('Level Information', {'fields': ['level_rank','tray_slots']})]
	inlines = [PositionInline]

class LevelInline(admin.StackedInline):
	model = Level
	extra = 0
	fieldsets = [('Level Information', {'fields': ['level_rank','tray_slots']})]

class UnitAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['unit_text','unit_height','unit_length']})]
	inlines = [LevelInline]

class UnitInline(admin.TabularInline):
	model = Unit
	extra = 0
	fieldsets = [(None, {'fields':['unit_text']}),
				('Dimensions', {'fields':['unit_height','unit_length']}),
				('Date Information', {'fields':['pub_date'], 'classes':['collapse']})]

class FarmAdmin(admin.ModelAdmin):
	fieldsets = [('AeroFarms', {'fields': ['farm_address']})]
	inlines = [UnitInline]

admin.site.register(Level, LevelAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Farm, FarmAdmin)