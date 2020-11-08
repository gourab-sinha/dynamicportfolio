from django.urls import path
from certifications.views import CertificateView

app_name='certificate'
urlpatterns = [
    path('certificates/', CertificateView.as_view(), name='certificates')
]