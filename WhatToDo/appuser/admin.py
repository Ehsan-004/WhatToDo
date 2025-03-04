from django.contrib import admin
from .models import AppUser



class AppUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth')
    search_fields = ('user',)
    # list_filter = ('published_date',)
    
admin.site.register(AppUser, AppUserAdmin)
