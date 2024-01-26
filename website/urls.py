from django.urls import path
from . import views as web_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', web_views.home, name='website-home'),
    path('about/', web_views.about, name='website-about'),
    path('ourwork/', web_views.ourwork, name='website-our-work'),
]