from django.contrib import admin
from Database.models import DatabaseModel

class DatabaseAdmin(admin.ModelAdmin):
    list_display=('plant_name', 'plant_family', 'plant_des')

admin.site.register(DatabaseModel, DatabaseAdmin)

# Register your models here.
