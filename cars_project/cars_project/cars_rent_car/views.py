from django.shortcuts import render, redirect

# Create your views here.
from cars_project.cars.models import Car
from cars_project.cars_rent_car.forms import RentCarForm
from cars_project.cars_rent_car.models import RentCar


def rent_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        form = RentCarForm(request.POST)

        if form.is_valid():
            rent = form.save(commit=False)
            rent.user = request.user
            rent.car = car
            rent.save()
            return redirect('rent cart')

    else:
        form = RentCarForm()

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'rent/rent_car_page.html', context)


def rent_cart(request):
    user = request.user

    current_user_rent = RentCar.objects.filter(user=user)


    context = {
        'current_user_rent': current_user_rent,
    }

    return render(request, 'rent/cars_rent_cart.html', context)