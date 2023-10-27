from django.urls import path
from . import views


urlpatterns = [
    path('', views.ActionRequestView.as_view()),
    path('<int:pk>', views.ActionRequestView.as_view())
    #path('api/due_date/', get_due_date, name='get_due_date')
]