from django.contrib.auth import login
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from airlines.models import Crew, Plane, Order, Client
from airlines.forms import PlaneCreateForm, OrderCreateForm


# @login_required
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


class CrewListView(generic.ListView):
    model = Crew
    context_object_name = "crew_list"
    template_name = "crew_list.html"
    paginate_by = 5


class CrewCreateView(generic.CreateView):
    model = Crew
    fields = "__all__"
    success_url = reverse_lazy("djangoProject:crew-list")


class CrewUpdateView(generic.UpdateView):
    model = Crew
    fields = "__all__"
    success_url = reverse_lazy("djangoProject:crew-list")


class CrewDeleteView(generic.DeleteView):
    model = Crew
    success_url = reverse_lazy("djangoProject:crew-list")


class PlaneListView(generic.ListView):
    model = Plane
    context_object_name = "plane_list"
    template_name = "plane_list.html"
    paginate_by = 5


class PlaneCreateView(generic.CreateView):
    model = Plane
    form_class = PlaneCreateForm
    template_name = "plane_form.html"
    success_url = reverse_lazy("plane-list")


class PlaneDetailView(generic.DetailView):
    model = Plane
    template_name = "plane_detail.html"
    context_object_name = "plane"
    queryset = Plane.objects.all().select_related("crew")


class PlaneUpdateView(generic.UpdateView):
    model = Plane
    template_name = 'plane_form.html'
    fields = "__all__"
    success_url = reverse_lazy("plane-list")


class PlaneDeleteView(generic.DeleteView):
    model = Plane
    template_name = "plane_confirm_delete.html"
    success_url = reverse_lazy("plane-list")


class OrderListView(generic.ListView):
    model = Order
    context_object_name = "order_list"
    template_name = "order_list.html"
    paginate_by = 5

class OrderCreateView(generic.CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = "order_form.html"
    success_url = reverse_lazy("order-list")

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "order_detail.html"
    context_object_name = "order"
    queryset = Order.objects.all().prefetch_related("flight")


class OrderUpdateView(generic.UpdateView):
    model = Order
    # form_class = OrderForm
    template_name = 'order_form.html'
    fields = '__all__'
    success_url = reverse_lazy("order-list")


class OrderDeleteView(generic.DeleteView):
    model = Order
    template_name = "order_confirm_delete.html"
    success_url = reverse_lazy("avia_company:order-list")


class ClientListView(generic.ListView):
    model = Client
    context_object_name = "client_list"
    paginate_by = 5


class ClientDetailView(generic.DetailView):
    model = Client
    context_object_name = "client"


class ClientUpdateView(generic.UpdateView):
    model = Client
    fields = "__all__"
    success_url = reverse_lazy("avia_company:client-list")


class ClientDeleteView(generic.DeleteView):
    model = Client
    success_url = reverse_lazy("avia_company:client-list")


class CustomLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("avia_company:index")


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("avia_company:index")
    success_url = reverse_lazy("avia_company:index")


def plane_list(request):
    planes = Plane.objects.all()
    paginator = Paginator(planes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'plane_list.html', {'page_obj': page_obj})


def crew_list(request):
    crews = Crew.objects.all()
    paginator = Paginator(crews, 5)  # 5 экипажей на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'crew_list.html', {'page_obj': page_obj})


