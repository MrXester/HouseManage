from django.urls import path, re_path
from django.urls import path
from .views import index
from django.contrib.auth.views import LogoutView

urlpatterns = [

    # The home page
    re_path(r'', index, name='indFit'),
]


