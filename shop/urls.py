from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.allProdCt, name='allProdCt'),
    path('<slug:c_slug>/', views.allProdCt, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proddetail, name='prodcatdetail'),

]
