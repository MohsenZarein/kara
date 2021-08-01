from django.urls import path
from . import views

urlpatterns = [
    path(
        'top-trade-streams/<str:symbol>',
        views.TradeStreamAPI.as_view(),
        name='top-ten-quantity-trades'
    ),
]
