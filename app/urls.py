

from django.contrib import admin
from django.urls import path
from .views import afghanistan_overview, history, diplomacy, culture, output_all_entries, Index

app_name = 'app'
urlpatterns = [
    path("Afghanistan/admin/", admin.site.urls),
    path('Afghanistan/index',Index.as_view(),name='index'),
    path('Afghanistan', afghanistan_overview, name='afghanistan_overview'),
    path('Afghanistan/history',history, name='history'),
    path('Afghanistan/diplomacy',diplomacy, name='diplomacy'),
    path('Afghanistan/culture',culture, name='culture'),
    path('Afghanistan/message', output_all_entries, name='message'),
]
