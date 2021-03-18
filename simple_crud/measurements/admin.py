from django.contrib import admin
from measurements.models import Measurement, Project


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
	pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	pass
