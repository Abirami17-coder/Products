from django.urls import path
from .views import *
urlpatterns = [
    path('home/',home,name='add'),
    path('front/',front),
    path('table/',table,name='fav'),
     path('delete/<str:id>/',delete_product,name='product_delete'),
    path('update/<str:id>/',update_product,name='product_update')
]

