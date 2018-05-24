from django.contrib import admin
from .models import Label,Bag

class LabelAdmin(admin.ModelAdmin):
    list_display = ('sku', 'header', 'fnsku', 'bag')
    prepopulated_fields = {'header': ('sku',)}

admin.site.register(Label, LabelAdmin)
admin.site.register(Bag)
