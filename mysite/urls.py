from django.contrib import admin
from django.urls import path, include
from myweb import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    #path('polls/', include('polls.urls')),
    path('myweb/', include('myweb.urls')),
    path('united', views.united),
    path('admin/', admin.site.urls),
    path('login/', views.loginPage),
    path('register/', views.registerPage),
    path('home/', views.home),
    path('logout/', views.logout),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
