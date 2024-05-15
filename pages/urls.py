from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('contact-me/', views.ContactMe.as_view(), name='contact_me'),
    path('about-me/', views.AboutMe.as_view(), name='about_me'),
    path('projects/', views.ProjectsView.as_view(), name='works'),
    path('credentials/', views.Credential.as_view(), name='credentials_page'),
    path('projects/<pk>', views.ProjectDetailView.as_view(), name='detail_page'),
    path('services/', views.ServicesView.as_view(), name='services_page'),
]
