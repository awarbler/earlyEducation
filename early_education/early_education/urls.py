"""early_education URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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


"""DO NOT USE THIS URLS FOR WEBSITE USE  THE WEBSITE URLS THIS IS NOT TO BE EDITED. """
from django.contrib import admin
from django.urls import path, include
"""DO NOT USE THIS URLS FOR WEBSITE USE  THE WEBSITE URLS THIS IS NOT TO BE EDITED. """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wesite.urls')),
]
