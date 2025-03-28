"""
URL configuration for minidouban project.

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
from movies import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from .views import movie_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('movies/', include('movies.urls')),
    path('book/', include('book.urls')),
    path('accounts/', include('accounts.urls')),
    path('search/', views.search, name='search'),
    path('movieticket/', movie_info, name='movie_info'),

]

# git status
# git add .
# git commit -m "添加了新的功能描述"
# git push origin main
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)