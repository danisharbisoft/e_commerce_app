from django.urls import path
from .views import cart_views, checkout_views, product_views

app_name = 'buyer'

urlpatterns = [
    path('', product_views.BuyerDashboard.as_view(), name='dashboard'),
    path('product_details/<int:pk>', product_views.ProductDetailView.as_view(), name='product_details'),
    path('cart', cart_views.CartItems.as_view(), name='cart'),
    path('add_to_cart/<int:id>', cart_views.add_to_cart, name='add_to_cart'),
    path('delete/<int:pk>', cart_views.RemoveFromCart.as_view(), name='delete'),
    path('checkout_logic', checkout_views.checkout_logic, name='checkout_logic'),
    path('checkout_form', checkout_views.CheckoutDetailsForm.as_view(), name='checkout_form'),
    path('confirmation', checkout_views.ConfirmationView.as_view(), name='confirmation'),
    path('success', checkout_views.SuccessView.as_view(), name='success')
]
