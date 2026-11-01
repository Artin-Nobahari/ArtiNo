from django.urls import path
from .views import *

app_name = "payment"

urlpatterns = [
    path("order-pay/", order_pay, name="order_pay"),
    path("verify-pay/", verify_pay, name="verify_pay"),
    path("start-pay/", start_pay, name="start_pay"),
]
