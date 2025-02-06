from django.shortcuts import render

from django.views.generic import TemplateView

class HomeTemplateView(TemplateView):
    template_name = 'index.html'

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

class ProductTemplateView(TemplateView):
    template_name = 'products.html'

class ProdctionTemplateView(TemplateView):
    template_name = 'production.html'

class DeliveryTemplateView(TemplateView):
    template_name = 'delivery.html'

class ContactTemplateViewSet(TemplateView):
    template_name = 'contacts.html'