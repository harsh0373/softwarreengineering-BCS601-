from django.contrib import admin
from .models import Program,Branch,Year,Material,Notification,Coarses,Centers

# Register your models here.
admin.site.register(Program)
admin.site.register(Branch)
admin.site.register(Year)
admin.site.register(Material)
admin.site.register(Notification)
admin.site.register(Coarses)
admin.site.register(Centers)

