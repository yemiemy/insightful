"""
URL configuration for insight project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from page.views import home,about,contact,service,summer,camp,blog,blog1,section,blog2,blog3,blog4,blog5,tutor,insight,daycare,study,store

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('about/', about,name='about'),
    path('contact/', contact,name='contact'),
    path('service', service,name='service'),
    path('summer/', summer,name='summer'),
    path('camp/', camp,name='camp'),
    path('blog/', blog,name='blog'),
    path('blog1/', blog1,name='blog1'),
    path('blog2/', blog2,name='blog2'),
    path('blog3/', blog3,name='blog3'),
    path('blog4/', blog4,name='blog4'),
    path('blog5/', blog5,name='blog5'),
    path('tutor/', tutor,name='tutor'),
    path('insight/', insight,name='insight'),
    path('daycare/', daycare,name='daycare'),
    path('study/', study,name='study'),
    path('store/', store,name='store'),
    path('section/<int:id>', section,name='section'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
