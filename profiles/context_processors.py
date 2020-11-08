# from profiles.models import Profile
# from django.shortcuts import get_list_or_404

# def profile(request):
#     context = {}
#     profile = get_list_or_404(Profile)[0]
#     context['profile'] = profile

#     list_skills = profile.skills_set
#     skills = {}
#     for skill in list_skills:
#         if skill.skill_type in skills:
#             skills[skill.skill_type].append(skill.title)
#         else:
#             skills[skill.skill_type] = [skill.title]
    
#     context['skills'] = skills
    
#     ach_list = profile.achievement_list
#     achievements = {}
#     for achievement  in ach_list:
#         achievements[achievement.title] = achievement.description
    
#     context['achievements'] = achievements
#     return context