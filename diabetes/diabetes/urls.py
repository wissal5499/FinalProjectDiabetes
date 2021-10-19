
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from .import views
from diabetesApp.views import tr,result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',tr, name='tr'),
    path("predict/result",result,name='submit_prediction'),
    url(r'^predict/$',views.predict),
    url(r'^base/$',views.base),
    url(r'^$',views.homepage),

    url(r'^causes/',include('diabetesApp.urls')),


]
