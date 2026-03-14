from django.contrib import admin
from .models import Assetowner, Asset, Scan, Vulnerabilitydefinition, Finding, Mitigationaction

# Register your models here.
admin.site.register(Assetowner)
admin.site.register(Asset)
admin.site.register(Scan)
admin.site.register(Vulnerabilitydefinition)
admin.site.register(Finding)
admin.site.register(Mitigationaction)
