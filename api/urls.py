from django.urls import path

from .views import GetUsersView

urlpatterns = [
    path('', GetUsersView.as_view())
]
