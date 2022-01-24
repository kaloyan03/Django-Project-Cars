from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

# Create your views here.
from cars_project.cars.models import Car
from cars_project.profiles.forms import ChangeProfilePhotoForm

UserModel = get_user_model()

def show_profile(request, pk):
    user_profile = UserModel.objects.get(pk=pk)
    profile_photo_form = ChangeProfilePhotoForm()
    current_profile_cars = Car.objects.filter(user=user_profile)
    context = {
        'profile': user_profile,
        'form': profile_photo_form,
        'cars': current_profile_cars,
    }
    return render(request, 'profile.html', context)


def change_profile_photo(request, pk):
    if request.method == 'POST':
        form = ChangeProfilePhotoForm(request.POST, request.FILES)

        if form.is_valid():
            user = UserModel.objects.get(pk=pk)
            profile_photo = form.cleaned_data['profile_photo']
            user.profile_photo = profile_photo
            user.save()
        return redirect('show profile', user.id)

