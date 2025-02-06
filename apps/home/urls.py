from django.urls import path
from .views import HomeTemplateView,AboutTemplateView,ProductTemplateView,ProdctionTemplateView,DeliveryTemplateView,ContactTemplateViewSet

urlpatterns = [
    path("",HomeTemplateView.as_view(),name="home"),
    path("about",AboutTemplateView.as_view(),name="about"),
    path('products',ProductTemplateView.as_view(),name='products'),
    path('production',ProdctionTemplateView.as_view(),name='production'),
    path('delivery',DeliveryTemplateView.as_view(),name='delivery'),
    path('contacts',ContactTemplateViewSet.as_view(),name='contacts'),
]