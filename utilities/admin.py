from django.contrib import admin

from .models import Hospital, License

class HospitalAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'address', 'state', 'services', 'equipment', 'radiographers')
  list_display_links = ('id', 'name')
  list_filter = ('name',)
  search_fields = ('name', 'address', 'state', 'services', 'equipment', 'radiographers')
  list_per_page = 25




class LicenseAdmin(admin.ModelAdmin):
  list_display = ('id', 'hospital_name', 'license_id', 'license_category', 'issue_date', 'expiry_date', 'status')
  list_display_links = ('id', 'hospital_name')
  list_filter = ('hospital_name',)
  #list_editable = ('license_id',)
  search_fields = ('hospital_name', 'license_id', 'license_category')
  list_per_page = 25

admin.site.register(Hospital, HospitalAdmin)
admin.site.register(License, LicenseAdmin)
