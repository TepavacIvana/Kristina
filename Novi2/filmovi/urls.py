from django.urls import path, include
from filmovi import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter


# API endpoints
urlpatterns = [
    path('filmovi/', views.FilmoviList.as_view()),
    path('filmovi/film', views.FilmoviDetail.as_view()),
    path('filmovi/<int:pk>/', views.FilmoviDetail.as_view()),
    path('filmovi/<str:zanr>/', views.FilmoviBy.as_view()),
    path('produkcija/', views.ProdukcijaList.as_view()),
    path('produkcija/<int:pk>/', views.ProdukcijaDetail.as_view()),
    path('bioskopi/', views.BioskopiList.as_view()),
    path('bioskopi/<int:pk>/', views.BioskopiDetail.as_view()),
]


