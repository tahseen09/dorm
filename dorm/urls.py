
from django.contrib import admin
from django.urls import path, include
from booking import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.dashboard, name="dashboard"),
    path('checkin', views.checkin, name="checkin"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
