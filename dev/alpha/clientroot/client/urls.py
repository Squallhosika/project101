"""unicorn URL Configuration

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
from django.conf.urls import url, include
from client.client import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'client/items', views.ItemViewSet)
router.register(r'client/menus', views.MenuViewSet)
router.register(r'client/clients', views.ClientViewSet)
router.register(r'client/menuitems', views.RNN_MenuItemViewSet)
router.register(r'client/clientmenus', views.RNN_ClientMenuViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^client/clientaround/', views.client_around),
    url(r'^client/createclient/', views.create_client),
    url(r'^client/createmenu/', views.create_menu),
    url(r'^client/createitem/', views.create_item),
    url(r'^client/updateclient/', views.update_client),
    url(r'^client/updatemenu/', views.update_menu),
    url(r'^client/updateitem/', views.update_item),
    url(r'^client/additemmenu/', views.add_item_to_menu),
    url(r'^client/removeitemmenu/', views.remove_item_from_menu),
    url(r'^client/itemmenus/', views.get_items_from_menu),
    url(r'^client/addmenuclient/', views.add_menu_to_client),
    url(r'^', include(router.urls))
]
