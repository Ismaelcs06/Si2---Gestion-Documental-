from django.urls import path
from .views import MeView, ChangePasswordView

urlpatterns = [
    path('me/', MeView.as_view(), name='me'),
    path('auth/change-password/', ChangePasswordView.as_view(), name='change-password'),
]
