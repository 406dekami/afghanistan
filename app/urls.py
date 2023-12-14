from django.contrib import admin
from django.urls import path

from . import views
from .views import afghanistan_overview, history, diplomacy, culture, output_all_entries, Index, contact, map, review

app_name = 'app'
urlpatterns = [
    path('Afghanistan/', afghanistan_overview, name='afghanistan_overview'),
    path("Afghanistan/admin/", admin.site.urls),
    path('Afghanistan/history/', history, name='history'),
    path('Afghanistan/diplomacy/', diplomacy, name='diplomacy'),
    path('Afghanistan/culture/', culture, name='culture'),
    path('Afghanistan/message/', output_all_entries, name='message'),
    path('Afghanistan/contact/', contact, name='contact'),
    path('Afghanistan/map/', map, name='map'),
    path('Afghanistan/review/', review, name='review'),
    path('process_form', views.process_form, name='process_form'),
]
