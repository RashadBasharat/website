from django.urls import path
from . import views

urlpatterns = [
        path('test', views.test, name="test"),
        path('create_user', views.create_user, name="create_user"),
        path('add_application', views.add_application, name="app_application"),
        path('new_user', views.new_user, name="new_user"),
        path('status', views.status, name="status"),
]
