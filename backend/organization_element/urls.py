from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrganizationElementView.as_view()),
    path('<int:pk>', views.OrganizationElementView.as_view())
]
