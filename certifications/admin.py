from django.contrib import admin
from certifications.models import Certificate
# Register your models here.

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display=('title', 'issued_by','slug', 'start_date', 'end_date', 'expire_date', 'is_lifetime_valid', 'image', 'verify_url', 'description', 'list_skills')
    list_filter=('title', 'issued_by', 'start_date')
    prepopulated_fields = {'slug': ('title',)}