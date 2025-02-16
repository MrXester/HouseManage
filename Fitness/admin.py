from django.contrib import admin
from .models import Metric

class MetricAdmin(admin.ModelAdmin):
    list_display= ("food","name","color")


admin.site.register(Metric,MetricAdmin)