# from django.conf.urls import url
from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^cart/$', views.cart, name='cart'),
    re_path(r'^menu/$', views.menu, name='menu'),
    re_path(r'^myorders/$', views.my_orders, name='my_orders'),
    
    re_path(r'^dashboard/admin/users/$', views.users_admin, name='users_admin'),
    re_path(r'^dashboard/admin/orders/$', views.orders_admin, name='orders_admin'),
    re_path(r'^dashboard/admin/foods/$', views.foods_admin, name='foods_admin'),
    re_path(r'^dashboard/admin/$', views.dashboard_admin, name='dashboard_admin'),
    re_path(r'^dashboard/admin/sales/$', views.sales_admin, name='sales_admin'),
    
    re_path(r'^dashboard/admin/users/add_user/$', views.add_user, name='add_user'),
    re_path(r'^dashboard/admin/foods/add_food/$', views.add_food, name='add_food'),
    re_path(r'^dashboard/admin/sales/add_sales/$', views.add_sales, name='add_sales'),
    re_path(r'^dashboard/admin/foods/editFood/(?P<foodID>\d+)/$', views.edit_food, name='edit_food'),
    re_path(r'^dashboard/admin/foods/foodDetails/(?P<foodID>\d+)/$', views.food_details, name='food_details'),
    re_path(r'^dashboard/admin/sales/editSale/(?P<saleID>\d+)/$', views.edit_sales, name='edit_sales'),
    
    re_path(r'^dashboard/admin/orders/confirm_order/(?P<orderID>\d+)/$', views.confirm_order, name='confirm_order'),
    re_path(r'^dashboard/admin/orders/confirm_delivery/(?P<orderID>\d+)/$', views.confirm_delivery, name='confirm_delivery'),
    
    re_path(r'^delete_item/(?P<ID>\d+)/$', views.delete_item, name='delete_item'),
    re_path(r'^add_deliveryBoy/(?P<orderID>\d+)/$', views.add_deliveryBoy, name='add_deliveryBoy'),
    re_path(r'^placeOrder/$', views.placeOrder, name='placeOrder'),
    re_path(r'^addTocart/(?P<foodID>\d+)/(?P<userID>\d+)/$', views.addTocart, name='addTocart'),

    re_path(r'^dashboard/delivery_boy/$', views.delivery_boy, name='delivery_boy'),
]
