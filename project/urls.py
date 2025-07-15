"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from accounts import views as account_views
from detect import views as detect_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('accounts.urls')),
    # path('detect/',include('detect.urls')),
    
    path('admin/', admin.site.urls),
    path('accounts/', include([
        path('register', account_views.register, name='register'),
        path('login', account_views.login, name='login'),
        path('logout', account_views.logout, name='logout'),
        path('about', account_views.about, name='about'),
        # path('home', account_views.home, name='home'),
        path('home',detect_views.detect_retinopathy,name='detect_retinopathy'),
        # path('result',detect_views.retino_result,name="retino_result"),
        path('history',detect_views.get_history,name="get_history"),
    ])),
    path('', account_views.home, name='home'),
    path('detect/', include('detect.urls')),
    
    path('detect/',include([
        path('upload',detect_views.detect_retinopathy,name='detect_retinopathy'),
        path('result',detect_views.retino_result,name="retino_result"),
        path('home', account_views.home, name='home'),
        path('about', account_views.about, name='about'),
    ])),
    path('detect/',detect_views.index,name="detect_page")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)