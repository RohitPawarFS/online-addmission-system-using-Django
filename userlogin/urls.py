"""userlogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from home.views import contact
from home import views

# from django.views.static import serve
# from django.conf.urls import url
# from django.urls import re_path
#dummy
#from django.conf import settings # new
#from django.conf.urls.static import static # new
#dummy

admin.site.site_header = "Online Admission Admin"
admin.site.site_title = "Online Admission Admin Portal"
admin.site.index_title = "Welcome to Rohit's Online Admission Managment System"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    # re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # path('upload/', views.contact)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#dummy
#if settings.DEBUG: # new
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#dummy