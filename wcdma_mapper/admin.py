from django.contrib import admin
from wcdma_mapper.models import RAitem, FeatureID, OSSitem


class RAitemAdmin(admin.ModelAdmin):
    list_display = ('item_code', 'description')


class FeatureIdAdmin(admin.ModelAdmin):
    list_display = ('feature_id', 'ra_item')


class OSSitemAdmin(admin.ModelAdmin):
    # !!! TODO: add column to display RA item also.
    # This requires a small revision of DB schema (look in models.py).
    list_display = ('item_code', 'description', 'feature_id')


admin.site.register(RAitem, RAitemAdmin)
admin.site.register(FeatureID, FeatureIdAdmin)
admin.site.register(OSSitem, OSSitemAdmin)
