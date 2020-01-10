from django.urls import path, include

from django.contrib import admin
from hello.views import index,Photos,fronts

urlpatterns = [
    path("",index),
    path("admin/", admin.site.urls),
    path('portfolio/',index),
    path('/form',Photos),
    path("portfolio/",fronts),
]
