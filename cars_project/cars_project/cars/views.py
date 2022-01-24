from django.shortcuts import render, redirect

# Create your views here.
from cars_project.cars.forms import AddCarForm
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

    return render(request, 'add_car_page.html', context)

def list_cars(request):
    cars = Car.objects.all()

    context = {
        'cars': cars,
    }

    return render(request, 'list_cars_page.html', context)