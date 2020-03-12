from django.urls import path
from . import views

urlpatterns = [

	path('',views.index,name="index"),
	path('hotel-list/',views.HotelListView.as_view(),name='hotel-list'),
	path('hotel-detail/',views.HotelDetailView.as_view(),name='hotel-detail'),
	path('roomfacility-list/',views.RoomFacList.as_view(),name='roomfac-list'),
	path('room-list/',views.RoomListView.as_view(),name='room-list'),
	path('room-detail/',views.RoomDetailView.as_view(),name='room-detail'),
	path('reservation-list/',views.ReservationListView.as_view(),name='reservation-list'),
	path('reservation-detail/',views.ReservationDetailView.as_view(),name='reservation-detail'),


]
