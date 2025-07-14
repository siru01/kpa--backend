from django.urls import path
from .views import WheelSpecCreateView, WheelSpecListView

urlpatterns = [
    path('wheel-specifications/', WheelSpecListView.as_view(), name='list-specs'),
    path('wheel-specifications/create/', WheelSpecCreateView.as_view(), name='create-spec'),
]
