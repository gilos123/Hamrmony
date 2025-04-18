from django.urls import path
from .views import index_view, contact_view, about_view,priority_shortcuts_view, cloud_salesforcepng_view,Purchase_Order_Tracking_view,recommendation_view, priority_view, SOX_requirements_view, Inserting_terminals_into_organization_view

urlpatterns = [
    path('', index_view, name='home'),  # this is your main page
    path('contact/', contact_view, name='contact'),  
    path('about/', about_view, name='about'),
    path('recommendation/', recommendation_view, name='recommendation'),
    path('priority/', priority_view,  name='priority'),
    path('priority/SOX_requirements/', SOX_requirements_view,  name='SOX_requirements'),
    path('priority/Purchase_Order_Tracking/', Purchase_Order_Tracking_view,  name='Purchase_Order_Tracking'),
    path('priority/priority_shortcuts/', priority_shortcuts_view,  name='priority_shortcuts'),
    path('priority/Inserting_terminals_into_organization/', Inserting_terminals_into_organization_view,  name='Inserting_terminals_into_organization'),
    path('cloud_salesforcepng/', cloud_salesforcepng_view,  name='cloud_salesforcepng'),
]