from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name='home'),
    path("register", views.register, name="register"),
    path("login", views.sign_in, name="login"),
    path("logout", views.signout, name="logout"),
    path('new', views.new, name='new'),
    path('edit/<int:id>', views.edit , name='edit'),
    path('complete/<int:id>', views.complete , name='complete')
]
