from django.urls import path
from trains import views

urlpatterns = [
    path('train_type/',
         views.TrainTypeView.as_view()),
]
