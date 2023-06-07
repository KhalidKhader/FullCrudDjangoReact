from django.contrib import admin
from .models import Employees
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display=("name","email","major","phone","age","created_at","updated_at")
    

admin.site.register(Employees,TodoAdmin)    