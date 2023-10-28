from django.urls import path
from . import views

urlpatterns = [
    path('', views.CorrespondentView.as_view()),
    path('<int:pk>', views.CorrespondentView.as_view())
]
