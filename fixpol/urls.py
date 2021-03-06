"""Defines URL patterns for users"""

from django.urls import path, include
from . import views

app_name = 'fixpol'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page that shows all locations.
    path('locations/', views.locations, name='locations'),

    # Page that shows all impacts.
    path('impacts/', views.impacts, name='impacts'),

    # Page for starting a search
    path('search/', views.search, name='search'),

    # Page for showing search results
    path('results/<int:search_id>/', 
            views.results, name='results'),

    # Page for showing search criteria
    path('criteria/<int:search_id>/', 
            views.criteria, name='criteria'),  

    # Page for saving or sharing results
    path('share/', views.share, name='share'),

    ]


