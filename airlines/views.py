from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from airlines.models import Crew, Plane, Order, Client


@login_required
def index(request):
    """View function for the home page of the site."""

    num_crews = Crew.objects.count()
    num_planes = Plane.objects.count()
    num_orders = Order.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_crews": num_crews,
        "num_planes": num_planes,
        "num_orders": num_orders,
        "num_visits": num_visits + 1,
    }

    return render(request, "index.html", context=context)


class CrewListView(LoginRequiredMixin, generic.ListView):
    model = Crew
    context_object_name = "crew_list"
    template_name = "crew_list.html"
    paginate_by = 5


class CrewCreateView(LoginRequiredMixin, generic.CreateView):
    model = Crew
    fields = "__all__"
    success_url = reverse_lazy("djangoProject:crew-list")


class CrewUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Crew
    fields = "__all__"
    success_url = reverse_lazy("djangoProject:crew-list")


class CrewDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Crew
    success_url = reverse_lazy("djangoProject:crew-list")


class PlaneListView(LoginRequiredMixin, generic.ListView):
    model = Plane
    context_object_name = "plane_list"
    template_name = "plane_list.html"
    paginate_by = 5


class PlaneDetailView(LoginRequiredMixin, generic.DetailView):
    model = Plane
    context_object_name = "plane"
    queryset = Plane.objects.all().select_related("planes__crew")


class PlaneUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Plane
    fields = "__all__"
    success_url = reverse_lazy("avia_company:plane-list")


class PlaneDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Plane
    success_url = reverse_lazy("avia_company:plane-list")


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    context_object_name = "order_list"
    paginate_by = 5


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Order
    context_object_name = "order"
    queryset = Order.objects.all().prefetch_related("flight")


class OrderUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Order
    fields = "__all__"
    success_url = reverse_lazy("avia_company:order-list")


class OrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Order
    success_url = reverse_lazy("avia_company:order-list")


class ClientListView(LoginRequiredMixin, generic.ListView):
    model = Client
    context_object_name = "client_list"
    paginate_by = 5


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Client
    context_object_name = "client"


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Client
    fields = "__all__"
    success_url = reverse_lazy("avia_company:client-list")


class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Client
    success_url = reverse_lazy("avia_company:client-list")

