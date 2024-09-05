from django.urls import path
import views

urlpatterns = [
    path('customers/', views.customers, name='customers'),
]