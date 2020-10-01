from django.contrib import admin
from django.urls import path,include
from trouble import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage/',include('mypage.urls')),
    path('trouble/', include(urls)),
    path('account/', include('account.urls')),
    path('account/',include('django.contrib.auth.urls')),
]
