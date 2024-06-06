from django.urls import path
from portfolio.views import *


app_name = 'portfolio'

urlpatterns = [
    path('', list, name='list'),
    path('<int:id>/', detail, name='detail'),
    path('yarat/', yarat, name='yarat'),
]