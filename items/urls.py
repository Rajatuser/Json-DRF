from .views import *
from django.urls import path


urlpatterns = [
    path('', RegisterUser.as_view(), name='Register'),
    path('login/', LoginView.as_view(), name='login'),
    path('data/', DataView.as_view(), name='data'),
    path('view/', DataView2.as_view(), name='view'),
]
