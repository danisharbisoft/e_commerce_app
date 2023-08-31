from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from seller.models import ProductModel


# Showing all products to the buyer
class BuyerDashboard(LoginRequiredMixin, ListView):
    template_name = 'buyer/dashboard.html'
    context_object_name = 'all_products'

    def get_queryset(self):
        return ProductModel.objects.all()


# Rendering the detail page for each product
class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'buyer/product_details.html'
    model = ProductModel
