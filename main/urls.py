from django.urls import path
from . import views

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('portfolio-detail/', views.PortfolioDetail, name='portfolio-detail'),
]