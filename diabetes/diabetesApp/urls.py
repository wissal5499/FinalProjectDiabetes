from django.conf.urls import url
from .import views
from django.urls import  path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.tr),
    url(r'^$',views.result),





]
