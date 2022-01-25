from django.shortcuts import render, redirect

# Create your views here.
from cars_project.cars.forms import AddCarForm, EditCarForm
from cars_project.cars.models import Car


def add_car(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('list cars')
    else:
        form = AddCarForm()

    context = {
        'form': form,
    }

    return render(request, 'cars/add_car_page.html', context)

def list_cars(request):
    cars = Car.objects.all()

    context = {
        'cars': cars,
    }

    return render(request, 'cars/list_cars_page.html', context)

def car_details(request, pk):
    car = Car.objects.get(pk=pk)
    is_owner = request.user.id == car.user.id
    context = {
        'car': car,
        'is_owner': is_owner,
    }

    return render(request, 'cars/car_details.html', context)


def edit_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditCarForm(request.POST, request.FILES, instance=car)

        if form.is_valid():
            form.save()
            return redirect('car details', car.id)
    else:
        form = EditCarForm(initial=car.__dict__)

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'cars/edit_car_page.html', context)

def delete_car(request, pk):
    if request.method == 'POST':
        car = Car.objects.get(pk=pk)
        car.delete()
        return redirect('list cars')

    else:
        car = Car.objects.get(pk=pk)

    context = {
        'car': car,
    }

    return render(request, 'cars/delete_car_page.html', context)

