from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from buyer.models import CartModel
from django.http import HttpResponseRedirect
from seller.models import ProductModel


# Handling the cart logic
class CartItems(LoginRequiredMixin, ListView):
    template_name = 'buyer/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return CartModel.objects.filter(user=self.request.user)

    def calculate_total_price(self):
        total_price = self.get_queryset().aggregate(total_price=Sum('product__product_price'))['total_price']
        return total_price

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_price'] = self.calculate_total_price()
        return context


def add_to_cart(request, id):
    product_instance = ProductModel.objects.get(pk=id)
    cart_item = CartModel.objects.create(product=product_instance, user=request.user)
    cart_item.save()
    return HttpResponseRedirect(reverse('buyer:cart'))


class RemoveFromCart(DeleteView):
    model = CartModel
    template_name = 'buyer/confirm_delete.html'
    success_url = reverse_lazy('buyer:cart')
