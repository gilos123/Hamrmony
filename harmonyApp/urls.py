from django.urls import path
from .views import index_view, contact_view, about_view, Purchase_Order_Tracking_view,recommendation_view, priority_view, SOX_requirements_view

urlpatterns = [
    path('', index_view, name='home'),  # this is your main page
    path('contact/', contact_view, name='contact'),  
    path('about/', about_view, name='about'),
    path('recommendation/', recommendation_view, name='recommendation'),
    path('priority/', priority_view,  name='priority'),
    path('priority/SOX_requirements/', SOX_requirements_view,  name='SOX_requirements'),
    path('priority/Purchase_Order_Tracking/', Purchase_Order_Tracking_view,  name='Purchase_Order_Tracking'),
]