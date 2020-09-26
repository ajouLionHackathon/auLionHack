from django.contrib import admin
from django.urls import path,include
import trouble.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trouble/',include('trouble.urls')),
]
