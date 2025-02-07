from django.shortcuts import render

from django.views.generic import TemplateView

from apps.home.models import Category

class HomeTemplateView(TemplateView):
    template_name = 'index.html'

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

class ProductTemplateView(TemplateView):
    template_name = 'products.html'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        categories = list(Category.objects.all())  # Convert queryset to list
        grouped_categories = [categories[i:i + 3] for i in range(0, len(categories), 3)]
        context["grouped_categories"] = grouped_categories
        return context
    

class ProdctionTemplateView(TemplateView):
    template_name = 'production.html'

class DeliveryTemplateView(TemplateView):
    template_name = 'delivery.html'

class ContactTemplateViewSet(TemplateView):
    template_name = 'contacts.html'