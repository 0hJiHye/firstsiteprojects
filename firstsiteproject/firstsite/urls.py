from django.contrib import admin
from django.urls import path
import hello.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello.views.home, name="home"),
    path('about/', hello.views.about, name="about"),
    path('result/', hello.views.result, name="result")
]
