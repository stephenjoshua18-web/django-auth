from django.urls import path
from .views import SignupAPIView, LoginAPIView, UserListView, DeleteUserView

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name ='users'),
    path('delete-user/<int:user_id>/', DeleteUserView.as_view(), name ='delete')
]
