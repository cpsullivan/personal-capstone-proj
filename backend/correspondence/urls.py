from django.urls import path
from . import views

urlpatterns = [
    path('', views.CorrespondenceView.as_view()),
    path('<int:pk>', views.CorrespondenceView.as_view())
]
