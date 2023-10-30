from django.contrib import admin
from .models import Status, Machine, Plant, Line, Scan

admin.site.register(Status)
admin.site.register(Machine)
admin.site.register(Scan)
admin.site.register(Line)
admin.site.register(Plant)