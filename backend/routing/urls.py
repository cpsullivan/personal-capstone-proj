from django.urls import path
from . import views


urlpatterns = [
    path('', views.RoutingView.as_view()),
    path('<int:pk>', views.RoutingView.as_view())
]