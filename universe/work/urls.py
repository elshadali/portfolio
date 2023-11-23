from django.urls import path
from .views import work_list, work_detail

urlpatterns = [
    path('work_list/', work_list, name='work'),
    path('work_list/<slug:work_slug>', work_detail, name='work_detail')
]
