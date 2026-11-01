from django.conf import settings
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse



# Create your views here.
def order_pay(request):
    data = {
        "merchant_id": settings.MERCHANT_ID,
        "amount": 1_000_000,
        "description": "Transaction description.",
        "callback_url": "http://127.0.0.1:8000/payment/verify-pay/",
    }

    response = requests.post(settings.REQUEST_PAY_API, data)

    if response.status_code == 200:
        json_response = response.json()
        authority = json_response['data']['authority']
        return redirect(f"{settings.START_PAY_API}/{authority}")
    else:
        return HttpResponse("connection fall!")


def verify_pay(request):
    return render(request, "payment/verify-pay.html")


def start_pay(request):
    # return render(request, "payment/start-pay.html")
    pass
