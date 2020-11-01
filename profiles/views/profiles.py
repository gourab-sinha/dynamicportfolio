from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from profiles.models import Profile, Skill


class ProfileView(TemplateView):
    template = 'profiles/profile.html'
    default_template = 'profile/setup.html'
    context = {}
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.all().first()
        
        if profile is None:
            return render(request, self.default_template, {})


        self.context['name'] = profile.name
        self.context['bio'] = profile.bio
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
        print(self.context['achievements'])
        return render(request, self.template, self.context)