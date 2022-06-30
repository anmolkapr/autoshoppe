
from locale import currency
from django.shortcuts import render
from django.conf import settings
import stripe
from django.views.generic.base import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
     
def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            currency='usd',
            description='Car payment',
            source= request.POST['stripeToken']
        )
        return render(request,'charge.html')