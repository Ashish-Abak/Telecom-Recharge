from django.contrib import admin
from rechargeapp.models import plan

# Register your models here.
class planAdmin(admin.ModelAdmin):
    list_display=['id','price','validity','data','is_active','total_data','voice','OTT','SMS']
    list_filter=['data','is_active']
admin.site.register(plan,planAdmin)
