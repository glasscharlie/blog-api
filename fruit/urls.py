from fruit.views import FruitList, FruitDetail
from django.urls import path


urlpatterns=[
    path('', FruitList.as_view(), name='post_list'),
    path('<int:pk>/', FruitDetail.as_view(), name='post_detail')
]