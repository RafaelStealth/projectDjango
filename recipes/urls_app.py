from django.urls import path
# from recipes.views import home, sobre
from . import views

urlpatterns = [
    path('', views.home),
    path('reciepes/<int:id>', views.recipe),
]
