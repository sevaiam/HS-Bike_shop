from django.urls import path
from .views import BikesView, OrderView

urlpatterns = [
    path("bikes/", BikesView.as_view()),
    path("bikes/<int:pk>/", BikesView.as_view()),
    path("order/<int:pk>/", OrderView.as_view(), name='order_no'),

]
