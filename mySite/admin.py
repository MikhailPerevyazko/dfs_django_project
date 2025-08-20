from django.contrib import admin
from .models import TrainingRegistration

# Register your models here.

@admin.register(TrainingRegistration)
class TrainingRegistrationAdmin(admin.ModelAdmin):
    list_display = ['child_name', 'phone_number', 'planned_date', 'created_at']
    list_filter = ['created_at', 'planned_date']
    search_fields = ['child_name', 'phone_number']
    ordering = ['-created_at']