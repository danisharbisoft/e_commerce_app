from django.shortcuts import reverse


def get_dashboard_url(person: str):
    if person == 'buyer':
        return reverse('buyer:dashboard')

    elif person == 'seller':
        return reverse('seller:dashboard')
