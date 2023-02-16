from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='index'),
    path('category/<slug:slug>/', SubCategoryPage.as_view(), name='category_page'),
]
