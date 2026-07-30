#Urls for the CRM app

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('contacts/', views.ContactListCreateView.as_view(), name='contact-list'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='contact-detail'),
    path('generate-draft/', views.GenerateDraftView.as_view(), name='generate-draft'),
]