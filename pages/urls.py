from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("market_update", views.MarketUpdateView.as_view(), name="market_update"),
]
