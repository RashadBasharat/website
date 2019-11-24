from django.urls import path
from . import views

urlpatterns = [
        path('test', views.test, name="test"),
        path('create_user', views.create_user, name="create_user"),
        path('add_application', views.add_application, name="app_application"),
]
