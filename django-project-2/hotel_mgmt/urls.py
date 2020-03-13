from django.urls import path
from . import views

urlpatterns = [

	path('',views.index,name="index"),
	path('roomtype-list/',views.RoomTypeView.as_view(),name='room-types'),
	path('roomtype/create/',views.RoomTypeCreateView.as_view(),name='room-types-create'),
	path('roomtype-detail/<int:pk>',views.RoomTypeDetailView.as_view(),name='room-type-detail'),
	path('roomfacility-list/',views.RoomFacList.as_view(),name='roomfac-list'),
	path('room-list/',views.RoomListView.as_view(),name='room-list'),
	path('room-detail/',views.RoomDetailView.as_view(),name='room-detail'),
	path('reservation-list/',views.ReservationListView.as_view(),name='reservation-list'),
	path('reservation-detail/',views.ReservationDetailView.as_view(),name='reservation-detail'),


]
