from django.urls import path, re_path
from django.urls import path
from .views import index,login_view,pages
from django.contrib.auth.views import LogoutView

urlpatterns = [

    # The home page
    path('', index, name='home'),
    path('login/', login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    re_path(r'^.*\.*', pages, name='pages'),
]


