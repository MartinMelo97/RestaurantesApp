from django.shortcuts import render, redirect
from django.views import View
from .models import RestaurantModel
from .forms import RestaurantForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
# Create your views here.


class RestaurantsListView(View):

    def get(self, request, *args, **kwargs):

        q = request.GET.get('q')
        template_name = "restaurantsapp/lista.html"
        restaurants = RestaurantModel.objects.all()
        if q:
            restaurants = RestaurantModel.objects.filter(
                Q(name__contains=q)|
                Q(owner__username__contains=q)|
                Q(platillos__nombre__contains=q)
            ).distinct()
        print(restaurants)
        context = {'restaurants':restaurants}

        return render(request, template_name, context)


class RestaurantsDetailView(View):

    @method_decorator(login_required)
    def get(self,request, pk):
        template_name = "restaurantsapp/detail.html"
        restaurant = RestaurantModel.objects.get(id=pk)
        context = {'restaurant': restaurant}

        return render(request, template_name, context)


class RestaurantCreateView(View):
    @method_decorator(login_required)
    def get(self, request):
        template_name = "restaurantsapp/restaurant_new.html"
        restaurantForm = RestaurantForm()
        context = {'form':restaurantForm}

        return render(request, template_name, context)

    def post(self, request):

        form = RestaurantForm(request.POST)

        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.owner = request.user
            form_data.save()

        return redirect('restaurants:list')


class RestaurantEditView(View):

    def get(self, request, pk):
        template_name="restaurantsapp/restaurant_new.html"
        restaurant = RestaurantModel.objects.get(id=pk)
        form = RestaurantForm(instance=restaurant)
        context = {'form':form}

        return render(request, template_name, context)

    def post(self, request, pk):

        restaurant = RestaurantModel.objects.get(id=pk)
        form = RestaurantForm(data=request.POST, instance=restaurant)

        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.save()

        return redirect('restaurants:detail', pk)


class RestaurantDeleteView(View):
    def get(self, request, pk):
        restaurant = RestaurantModel.objects.get(id=pk)
        restaurant.delete()

        return redirect('restaurants:list')
