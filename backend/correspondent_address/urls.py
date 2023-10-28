from django.urls import path
from . import views


urlpatterns = [
    path('', views.CorrespondentAddressView.as_view()),
    path('<int:pk>', views.CorrespondentAddressView.as_view())
]