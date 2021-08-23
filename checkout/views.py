from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JRga7DNcBrYrm0FIdq1r2gsBwWiogHuThxBZUoqroW2SnVqnTKr1e9nGrU1f7tUdRjN1G7CnxG123p3TJW3snYB00f0BkqO3m',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)