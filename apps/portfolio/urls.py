from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('api/home/', HomeAPIView.as_view(), name='home_api'),
    path('api/offers/', WebDevelopmentOfferAPIView.as_view(),
         name='webdevelopmentoffer_api'),
    path('api/card/', WebDevelopmentCardAPIView.as_view(),
         name='webdevelopmentcard_api'),
    path('api/technologies/', WebDevelopmentTechnologiesAPIView.as_view(),
         name='webdevelopmenttechnologies_api'),
    path('api/projects/', WebDevelopmentProjectsAPIView.as_view(),
         name='webdevelopmentprojects_api'),
    path('api/resume/', ResumeMEAPIView.as_view(), name='ResumeME'),
    path('api/contact/', ContactAPIView.as_view(), name='Contact')
]
