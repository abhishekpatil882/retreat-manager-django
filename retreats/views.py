from django.shortcuts import render
from rest_framework import generics, filters, serializers
from .models import Retreat, Booking
from .serializers import RetreatSerializer, BookingSerializer

class RetreatList(generics.ListCreateAPIView):
    queryset = Retreat.objects.all()
    serializer_class = RetreatSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'location']
    ordering_fields = ['price', 'duration']

class BookingCreate(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        retreat = serializer.validated_data.get('retreat')
        user_id = serializer.validated_data.get('user_id')
        if Booking.objects.filter(retreat=retreat, user_id=user_id).exists():
            raise serializers.ValidationError("This retreat is already booked for the user.")
        serializer.save()
