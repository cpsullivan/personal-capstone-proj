from django.urls import path
from . import views


urlpatterns = [
    path('', views.ResponseDocumentView.as_view()),
    path('<int:pk>', views.ResponseDocumentView.as_view())
]