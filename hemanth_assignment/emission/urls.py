from django.urls import path
from . import views

urlpatterns = [
    path('emissions/', views.EmissionsList.as_view(), name='emissions-list'),
    path('emissions/<int:pk>/', views.EmissionsDetail.as_view(), name='emissions-detail'),
]