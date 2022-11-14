from django.contrib import admin
from .models import Doctors, Directions


class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',
                    'description',
                    'work_experience',
                    )
    list_editable = ('slug',
                     'description',
                     'work_experience',
                     )
    list_filter = ('name',
                   'slug',
                   'directions'
                   )


class DirectionsAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Doctors, DoctorsAdmin)
admin.site.register(Directions, DirectionsAdmin)


