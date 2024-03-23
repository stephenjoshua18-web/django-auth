from django.urls import path
from .views import SignupAPIView, LoginAPIView, UserListView

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name ='users')
]
