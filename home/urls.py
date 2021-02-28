from .import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    
    path('education',views.education,name='education'),
    path('skills',views.skills,name='skills'),
    path('contact',views.submit,name='contact'),
]
