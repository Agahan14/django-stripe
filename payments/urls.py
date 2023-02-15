from django.urls import path

from . import views

urlpatterns = [
    path("buy/<int:item_id>", views.buy_item, name="buy"),
    path("item/<int:item_id>", views.item_details, name="item"),
    path('order/<int:order_id>', views.order_details, name='order'),
    path('buy_order/<int:order_id>', views.buy_order, name='buy_order'),
    path('index/', views.index, name='index')

]
