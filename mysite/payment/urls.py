from django.urls import path
from . import views

app_name = "payment"
urlpatterns = [
    path('<int:order_id>', views.charge, name="charge")
]
