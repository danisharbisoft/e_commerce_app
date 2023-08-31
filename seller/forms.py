from django import forms


class ProductForm(forms.Form):
    product_name = forms.CharField(label='Product Name', max_length=100, required=True)
    product_description = forms.CharField(label='Product Description', max_length=500, required=False,
                                          widget=forms.Textarea)
    product_price = forms.IntegerField(label='Price', required=True)
    product_image = forms.ImageField(label='Image')
