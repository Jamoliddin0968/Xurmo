from django.urls import path
# from .views import HomeTemplateView,AboutTemplateView,ProductTemplateView,ProdctionTemplateView,DeliveryTemplateView,ContactTemplateViewSet
from .views import HomePageView
urlpatterns = [
   path('index/', HomePageView.as_view(), name='home'),
]