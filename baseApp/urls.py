from django.urls import path
from .views import ClassBookingCreateView,ClassBookingListView,FitnessClassListCreateView

urlpatterns = [
    path('classes/', FitnessClassListCreateView.as_view()),
    path('book/', ClassBookingCreateView.as_view()),
    path('bookings/', ClassBookingListView.as_view()),
]
