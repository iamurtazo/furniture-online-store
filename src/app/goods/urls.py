from django.urls import path
from goods.views import CatalogView, ProductDetailView

app_name = 'goods'

urlpatterns = [
    path('search/', CatalogView.as_view(), name='search'),
    path('<slug:category_slug>/', CatalogView.as_view(), name='index'),
    path('product/<int:product_id>', ProductDetailView.as_view(), name='product'),
]