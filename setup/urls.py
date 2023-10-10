from django.contrib import admin
from django.urls import path

from app.views import home,outra_view

urlpatterns = [
    path('', home, name='home'),
    path('xpto',home,name='home2'),
    path('outra-rota',outra_view,name="outra_rota"),
    path('admin/', admin.site.urls),
]
