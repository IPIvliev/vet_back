from django.contrib import admin
from objects.models import Object, Customer, ObjectType, CustomerType

@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
  list_display = ['name', 'object_type', 'object_address']
  search_fields = ['name', 'object_address', 'object_type']
  ordering = ['-object_type']

@admin.register(Customer)
class PipeAdmin(admin.ModelAdmin):
  list_display = ['name', 'customer_type', 'customer_address']
  search_fields = ['name', 'customer_address', 'customer_type']
  ordering = ['-customer_type']

@admin.register(ObjectType)
class ObjectTypeAdmin(admin.ModelAdmin):
  list_display = ['name']

@admin.register(CustomerType)
class CustomerTypeAdmin(admin.ModelAdmin):
  list_display = ['name']