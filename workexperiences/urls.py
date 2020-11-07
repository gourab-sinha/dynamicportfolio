from django.urls import path
from workexperiences.views import CompanyView, CompanyDetailView

app_name='company'
urlpatterns = [
    path('workexperiences/', CompanyView.as_view(), name='companies'),
    path('workexperiences/<int:company_id>/', CompanyDetailView.as_view(), name='companydetail'),
]