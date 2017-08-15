"""order URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from order.order import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'order/items', views.ItemViewSet)
router.register(r'order/orders', views.OrderViewSet)
# router.register(r'order/orderflows', views.OrderFlowViewSet)
# router.register(r'order/queues', views.QueueViewSet)
router.register(r'order/orderitems', views.RNN_OrderItemViewSet)
# router.register(r'order/queueorders', views.RNN_QueueOrderViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'order/createitem', views.create_item),
    url(r'order/createorder', views.create_order),
    url(r'order/orderadditem', views.order_add_item),
    url(r'order/itemsbyorder', views.items_by_order),
    url(r'order/orderbyclientstatus', views.get_orders_by_client_status),
    url(r'order/ordervalidate', views.order_validate),
    url(r'order/orderreject', views.order_reject),
    url(r'order/orderstatus', views.order_status),
    url(r'order/orderpickup', views.order_pickup),
]
