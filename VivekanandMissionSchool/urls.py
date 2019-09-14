from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from MainApp import views
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('mission/',views.Mission),
    path('rules/',views.Rules),
    path('admission/',views.Admision),
    path('features/',views.Features),
    path('about/',views.About),
    path('principle/',views.Principle),
    path('sports/',views.Sports),
    path('images/',views.Images),
    path('contact/',views.Contactus),
    path('news/<int:num>',views.NewsPage),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
