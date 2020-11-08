from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_list_or_404
from profiles.models import Profile


class ProfileView(TemplateView):
    template = 'profiles/profile.html'
    default_template = 'profile/setup.html'
    context = {}
    def get(self, request, *args, **kwargs):
        profile = get_list_or_404(Profile)[0]

        self.context['profile'] = profile
        list_skills = profile.skills_set
        skills = {}
        for skill in list_skills:
            if skill.skill_type in skills:
                skills[skill.skill_type].append(skill.title)
            else:
                skills[skill.skill_type] = [skill.title]
        
        self.context['skills'] = skills
        
        ach_list = profile.achievement_list
        achievements = {}
        for achievement  in ach_list:
            achievements[achievement.title] = achievement.description
        
        self.context['achievements'] = achievements
        return render(request, self.template, self.context)