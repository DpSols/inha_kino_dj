from django.urls import path
from . import views


urlpatterns = [
    path('', views.MovieMainView.as_view()),

]
