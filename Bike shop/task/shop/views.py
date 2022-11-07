from django.views import View
from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Bike, Order, Basket


# Create your views here.


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'phone_number']
        labels = {
            'name': 'your name',
            'surname': 'your surname',
            'phone_number': 'your phone number',
        }


class BikesView(View):
    def get(self, request, *args, **kwargs):
        bikes = Bike.objects.all()
        if kwargs:
            bike_id = self.kwargs['pk']
            bike = Bike.objects.filter(id=bike_id).first()
            if bike:
                avail = False
                if bike.tire.quantity > 1 and bike.frame.quantity > 0 and bike.seat.quantity > 0 and (
                        (bike.has_basket and Basket.quantity) or bike.has_basket is False):
                    avail = True

                f = OrderForm
                return render(request, "shop/bike.html", {
                    "bike": bike, "form": f, "avail": avail
                })
        return render(request, "shop/index.html", {
            "bikes": bikes,
        })

    def post(self, request, *args, **kwargs):
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            bike_id = self.kwargs["pk"]
            new_order = order_form.save(commit=False)
            new_order.bike = Bike.objects.get(id=bike_id)
            new_order.status = ('P')

            new_order.bike.tire.quantity -= 2
            new_order.bike.tire.save()
            new_order.bike.frame.quantity -= 1
            new_order.bike.frame.save()
            new_order.bike.seat.quantity -= 1
            new_order.bike.seat.save()
            if new_order.bike.has_basket:
                basket = Basket.objects.get()
                basket.quantity -= 1
                basket.save()

            new_order.save()

        return HttpResponseRedirect(reverse("order_no", args=(new_order.id,)))


class OrderView(View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs["pk"])
        return render(request, "shop/order.html", {
            "order": order
        })





