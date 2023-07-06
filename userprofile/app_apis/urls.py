from django.urls import path
from . import views


urlpatterns=[
    path('cart-list-api/',views.AppAPIsUserCartModelListAPIView.as_view(),name='AppAPIsUserCartModelListAPIView'),
    path('add-to-cart-api/<id>/',views.AppAPIsUserCartModelAddItemGenericAPIView.as_view(),name='AppAPIsUserCartModelAddItemGenericAPIView'),
    path('remove-from-cart-api/<id>/',views.AppAPIsUserCartModelRemoveItemGenericAPIView.as_view(),name='AppAPIsUserCartModelRemoveItemGenericAPIView'),
    
]