from django.contrib import admin
from .models import WYR_Users, Category, Scenario

# Register your models here.
admin.site.register(WYR_Users)
admin.site.register(Category)
admin.site.register(Scenario)