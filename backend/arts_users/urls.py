from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArtsUserView.as_view()),
    path('<int:pk>', views.ArtsUserView.as_view())
]