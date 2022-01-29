from django.shortcuts import render, redirect

# Create your views here.
from cars_project.cars.forms import AddCarForm, EditCarForm, CommentForm
from cars_project.cars.models import Car, Comment, Like


def add_car(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST, request.FILES)

        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
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

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            message = comment_form.cleaned_data['message']
            comment = Comment(message=message, user=request.user, car=car)
            comment.save()
            return redirect('car details', car.id)



    else:
        comment_form = CommentForm()
        comments = Comment.objects.filter(car_id=car.id)
        is_owner = request.user.id == car.user.id
        car_likes_count = car.like_set.count()
        already_liked = bool(Like.objects.filter(user=request.user))

        context = {
            'car': car,
            'is_owner': is_owner,
            'comment_form': comment_form,
            "comments": comments,
            "car_likes_count": car_likes_count,
            'already_liked': already_liked,
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


def like_car(request, pk):
    car = Car.objects.get(pk=pk)

    like_object_by_user = Like.objects.filter(user=request.user)

    if like_object_by_user:
        like_object_by_user.delete()
    else:
        like = Like(
            car=car,
            user=request.user,
        )

        like.save()

    return redirect('car details', car.id)
