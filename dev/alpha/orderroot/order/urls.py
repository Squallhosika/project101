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
router.register(r'order/orderitems', views.RNN_OrderItemViewSet)
router.register(r'order/queues', views.QueueViewSet)
router.register(r'order/orderinqueues', views.OrderInQueueViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url('order/createorder', views.create_order),
    url('order/orderadditem', views.order_add_item),
    # url('order/itemsbyorder', views.items_by_order),
    url('order/placeorder', views.place_order),
    url('order/cancelorder', views.cancel_order),
    url('order/completeorder', views.complete_order),
    # url('order/queueposition', views.queue_position),
    url('order/createqueue', views.create_queue),
    url('order/deletequeue', views.delete_queue),
    # url('order/ordersinqueue', views.orders_in_queue),
    url('order/orderstatus', views.order_status)
]