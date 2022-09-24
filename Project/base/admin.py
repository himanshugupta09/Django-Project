from django.contrib import admin
from base.models import Service

class  ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon','service_title','service_des')

admin.site.register(Service,ServiceAdmin)    
# Register your models here.
