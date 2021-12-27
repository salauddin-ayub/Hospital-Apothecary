from django.contrib import admin
from register.models import Profile

# Register your models here.

@admin.register(Profile)
class EmployeeAdmin(admin.ModelAdmin):
    pass
