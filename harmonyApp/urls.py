from django.urls import path
from .views import index_view, contact_view, about_view, recommendation_view, priority_view

urlpatterns = [
    path('', index_view, name='home'),  # this is your main page
    path('contact/', contact_view, name='contact'),  
    path('about/', about_view, name='about'),
    path('recommendation/', recommendation_view, name='recommendation'),
    path('priority/', priority_view,  name='priority')
]