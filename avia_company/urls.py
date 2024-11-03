"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from airlines.views import (
    index,
    CrewListView,
    CrewCreateView,
    CrewUpdateView,
    CrewDeleteView,
    PlaneListView,
    PlaneCreateView,
    PlaneDetailView,
    PlaneUpdateView,
    PlaneDeleteView,
    OrderListView,
    OrderCreateView,
    OrderDetailView,
    OrderUpdateView,
    OrderDeleteView,
    ClientListView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView
)

app_name = "airlines"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("crew/", CrewListView.as_view(), name="crew-list"),
    path("crew/create", CrewCreateView.as_view(), name="crew-create"),
    path("crew/update/<int:pk>", CrewUpdateView.as_view(), name="crew-update"),
    path("crew/delete/<int:pk>", CrewDeleteView.as_view(), name="crew-delete"),
    path("plane/", PlaneListView.as_view(), name="plane-list"),
    path("plane/create", PlaneCreateView.as_view(), name="plane-create"),
    path("plane/<int:pk>", PlaneDetailView.as_view(), name="plane-detail"),
    path("plane/update/<int:pk>", PlaneUpdateView.as_view(), name="plane-update"),
    path("plane/delete/<int:pk>", PlaneDeleteView.as_view(), name="plane-delete"),
    path("order/", OrderListView.as_view(), name="order-list"),
    path("order/create/", OrderCreateView.as_view(), name="order-create"),
    path("order/<int:pk>", OrderDetailView.as_view(), name="order-detail"),
    path("order/update/<int:pk>", OrderUpdateView.as_view(), name="order-update"),
    path("order/delete/<int:pk>", OrderDeleteView.as_view(), name="order-delete"),
    path("client/", ClientListView.as_view(), name="client-list"),
    path("client/<int:pk>", ClientDetailView.as_view(), name="client-detail"),
    path("client/update/<int:pk>", ClientUpdateView.as_view(), name="client-update"),
    path("client/delete/<int:pk>", ClientDeleteView.as_view(), name="client-delete"),
]
