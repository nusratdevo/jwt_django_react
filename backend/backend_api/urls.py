
from rest_framework.routers import DefaultRouter
from backend_api import views
from django.urls import path

from backend_api.views import UserRegistrationView,UserLoginView, UserProfileView,  MovieView
urlpatterns = [
    path('/register', UserRegistrationView.as_view(), name='register'),
    path('/login', UserLoginView.as_view(), name='login'),
    path('/profile', UserProfileView.as_view(), name='profile'),
    
]
# router = DefaultRouter()
# router.register(r'movies', views.MovieViewSet, name='movie')
# urlpatterns = router.urls

