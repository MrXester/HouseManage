"""HouseManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("fit/", include("Fitness.urls")),
    path("finance/", include("Finances.urls"),name="finance"),
    path("unicorn/", include("django_unicorn.urls")),
    path("", include("Home.urls")),
]



handler404 = 'Finances.views.page_not_found'
handler403 = 'Finances.views.page_forbiden'
handler500 = 'Finances.views.page_error'