from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$', views.LoginView, name='login'),
    url(r'^accounts/logout/$', views.LogoutView, name='logout', kwargs={'next_page': '/'}),
]

