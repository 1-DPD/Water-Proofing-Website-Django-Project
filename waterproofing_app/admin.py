from django.contrib import admin
from .models import Service, Inquiry

# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service', 'created_at')
    list_filter = ('service', 'created_at')
    search_fields = ('customer__username', 'message')
    readonly_fields = ('customer', 'service', 'message', 'created_at')
