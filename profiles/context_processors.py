from profiles.models import Profile

def profile(request):
    context = {}
    profile = Profile.objects.all()[0]
    context['profile'] = profile

    list_skills = profile.skills_set
    skills = {}
    for skill in list_skills:
        if skill.skill_type in skills:
            skills[skill.skill_type].append(skill.title)
        else:
            skills[skill.skill_type] = [skill.title]
    
    context['skills'] = skills
    
    ach_list = profile.achievement_list
    achievements = {}
    for achievement  in ach_list:
        achievements[achievement.title] = achievement.description
    
    context['achievements'] = achievements
    return context