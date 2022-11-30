from django.urls import path
from trains import views

urlpatterns = [
    path('train_type/',
         views.TrainTypeView.as_view()),
    path('coach_composition/',
         views.CoachCompisitionView.as_view()),
    path('train_composition/',
         views.TrainCompoisitionView.as_view()),
    path('train_coach/',
         views.TrainCoachCompoisitionView.as_view()),
]
