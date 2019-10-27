from django.contrib import admin

from .models import Hospital, License, Centre

class HospitalAdmin(admin.ModelAdmin):
  list_display = ('id', 'hospital_name', 'address', 'state', 'services', 'equipment', 'radiographers')
  list_display_links = ('id', 'hospital_name')
  list_filter = ('hospital_name',)
  search_fields = ('hospital_name', 'address', 'state', 'services', 'equipment', 'radiographers')
  list_per_page = 25




class LicenseAdmin(admin.ModelAdmin):
  list_display = ('id', 'hospital_name', 'license_id', 'license_category', 'issue_date', 'expiry_date', 'status')
  list_display_links = ('id', 'hospital_name')
  list_filter = ('hospital_name',)
  #list_editable = ('license_id',)
  search_fields = ('hospital_name', 'license_id', 'license_category')
  list_per_page = 25



class CentreAdmin(admin.ModelAdmin):
  list_display = ('id', 'centre_name', 'rc_number', 'phone', 'email', 'state', 'city','address')
  list_display_links = ('id', 'centre_name')
  list_filter = ('centre_name',)
  search_fields = ('centre_name', 'rc_number', 'phone', 'email', 'state', 'city','address')
  list_per_page = 25

admin.site.register(Hospital, HospitalAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(Centre, CentreAdmin)
