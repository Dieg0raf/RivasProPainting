from . import views as contact_views
from django.urls import path

urlpatterns = [
    path('', contact_views.contact, name='website-contact'),
]