from django.urls import path
from .views import SignupAPIView, LoginAPIView, UserListView, DeleteUserView, BlockUserView, UnblockUserView

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name ='users'),
    path('delete-user/<int:user_id>/', DeleteUserView.as_view(), name ='delete'),
    path('block/', BlockUserView.as_view(), name='block'),
    path('unblock/', UnblockUserView.as_view(), name='unblock')
]
