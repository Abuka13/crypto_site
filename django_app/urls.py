from django.urls import path
from django_app import views
urlpatterns = [
    path("home/", views.home, name="home"),
    path("nav/", views.nav, name="nav"),
    path("posts/", views.posts, name="posts"),
    path("money/", views.money, name="money"),
    path("blockchain/", views.blockchain, name="blockchain"),
path("defi/", views.defi, name="defi"),
path("coins/", views.coins, name="coins"),
path("solidity/", views.solidity, name="solidity"),
path("exchanges/", views.exchanges, name="exchanges"),


#TODO
    path("posts/<str:pk>/", views.post1, name="post1"),
    ]