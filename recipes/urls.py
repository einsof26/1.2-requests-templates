from django.contrib import admin
from django.urls import path

from calculator.views import index


urlpatterns = [
    path('<recipe>/' , index, name = 'index'),
    path('admin/', admin.site.urls),
]
