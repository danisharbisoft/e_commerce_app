from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('product_detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('add_product', views.AddProductForm.as_view(), name='add_product'),
    path('delete/<int:pk>', views.DeleteProduct.as_view(), name='delete')
]
