from django.urls import path
from profiles.views import ProfileView

app_name = 'profile'
urlpatterns = [
    path('', ProfileView.as_view(), name='home'),
]