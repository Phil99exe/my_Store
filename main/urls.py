from django.urls import path
from django.utils.translation.trans_real import catalog

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.product_list, name='index'),
    path('catalog/', views.CatalogView.as_view(), name='catalog_all'),
    path('catalog/<slug:category_slug>/', views.CatalogDetailView.as_view(), name='catalog'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),

]