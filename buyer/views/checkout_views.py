from django.views.generic import TemplateView
from django.shortcuts import reverse,render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic import FormView
from buyer.forms import ShippingForm
from buyer.models import ShippingDetails,CartModel


# Handling checkout
def checkout_logic(request):
    if ShippingDetails.objects.filter(user=request.user):
        return HttpResponseRedirect(reverse('buyer:confirmation'))
    else:
        return HttpResponseRedirect(reverse('buyer:checkout_form'))


class CheckoutDetailsForm(FormView):
    template_name = 'buyer/checkout_form.html'
    form_class = ShippingForm

    def form_valid(self, form):
        data = form.cleaned_data
        shipping_details = ShippingDetails(
            user=self.request.user,
            name=data['name'],
            address=data['address'],
            city=data['city'],
            email=data['email']

        )
        shipping_details.save()
        return HttpResponseRedirect(reverse('buyer:confirmation'))


class ConfirmationView(TemplateView):
    template_name = 'buyer/confirm_order.html'


class SuccessView(TemplateView):
    template_name = 'buyer/success.html'

    def get(self, request, *args, **kwargs):
        recipient = ShippingDetails.objects.get(user=request.user)
        recipient_email = recipient.email
        send_order_confirmation_email(recipient_email)
        CartModel.objects.filter(user=self.request.user).delete()
        return render(request, self.template_name)


def send_order_confirmation_email(recipient_email):
    subject = 'Order Confirmation'
    message = 'Thank you for your order!It will be delivered within 5 workiing days'
    from_email = 'danishabbas2004@gmail.com'
    recipient_list = [recipient_email]
    send_mail(subject, message, from_email, recipient_list)
