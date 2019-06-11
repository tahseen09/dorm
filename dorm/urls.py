
from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.index, name="home"),
    path('checkin', views.checkin, name="checkin"),
    #path("checkout", views.checkout, name="checkout"),
]
