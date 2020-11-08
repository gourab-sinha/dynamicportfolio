from django.contrib import admin
from workexperiences.models import Company, CompanyProject, Technology


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'role', 'joining_date',
                    'list_projects', 'list_techs', 'currently_working')
    list_filter = ('name', 'joining_date','ending_date', )
    prepopulated_fields = {'slug': ('name','role')}

@admin.register(CompanyProject)
class CompanyProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'reporting_manager','start_date', 
                    'end_date', 'image','description','verify_url')
    list_filter = ('title', 'start_date', 'end_date')
    prepopulated_fields = {'slug': ('title','reporting_manager')}

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'tech_type')
    list_filtere = ('name', 'tech_type')
    prepopulated_fields = {'slug': ('name','tech_type')}



