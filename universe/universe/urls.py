from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('about.urls')),
    path('', include('core.urls')),
    path('', include('contact.urls')),
    path('', include('work.urls'))
]
