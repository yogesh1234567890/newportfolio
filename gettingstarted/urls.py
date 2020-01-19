from django.urls import path, include

from django.contrib import admin

from hello import views
urlpatterns = [
    path("front/",views.index),
    path("admin/", admin.site.urls),
    path('portfolio/',views.index,name="home"),
    path('form/',views.Photos),
    # path("portfolio/",views.fronts),
    path("register/",views.registerPage,name="register"),
    path("login/",views.loginPage,name="login"),
    path("logout/",views.logoutUser,name="logout"),
    path('^oauth/', include('social_django.urls', namespace='social')),
]
