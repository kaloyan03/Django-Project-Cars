from django.core.mail import send_mail
from django.db.models import F
from django.shortcuts import render, redirect

# Create your views here.
from cars_project.cars.models import Car
from cars_project.cars_rent_car.forms import RentCarForm, SendEmailForm
from cars_project.cars_rent_car.models import RentCar
from cars_project.settings import EMAIL_HOST_USER


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

    current_user_rent = RentCar.objects.filter(user=user).annotate(
        rent_for=F('date_end_rent') - F('date_start_rent'))

    total_price = sum([r.car.price for r in current_user_rent])
    if request.method == 'POST':
        send_email_form = SendEmailForm(request.POST)

        if send_email_form.is_valid():
            for rent in current_user_rent:
                rent.delete()

            subject = 'Thanks for your order'
            message = 'There is total price for your order: 1000$'
            recipient = send_email_form.cleaned_data['email']
            send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
            return redirect('rent cart')
    else:
        send_email_form = SendEmailForm()

        context = {
            'current_user_rent': current_user_rent,
            'send_email_form': send_email_form,
            'total_price': total_price,
        }

        return render(request, 'rent/cars_rent_cart.html', context)

# def send_email(request):
#     send_email_form = SendEmailForm(request.POST)
#
#     if send_email_form.is_valid():
#         subject = 'Thanks for your order'
#         message = 'There is total price for your order: 1000$'
#         recipient = send_email_form.cleaned_data['email']
#         send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
#         return redirect('list cars')