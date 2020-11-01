from django.contrib import admin
from profiles.models import Profile, Skill, Achievement
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'skills_set', 'achievement_list',)
    list_filter = ('name', )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'skill_type')
    list_filter = ('skill_type',)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title', )