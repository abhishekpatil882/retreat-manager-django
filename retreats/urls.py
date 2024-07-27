from django.urls import path
from .views import RetreatList, BookingCreate

urlpatterns = [
    path('retreats/', RetreatList.as_view(), name='retreat-list'),
    path('book/', BookingCreate.as_view(), name='booking-create'),
]