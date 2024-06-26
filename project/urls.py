from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from coffee.views import index, coffee_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('coffee.urls')),
    path('menu/', index, name='menu'),
    path('menu/<int:pk>/', coffee_detail, name='coffee-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
