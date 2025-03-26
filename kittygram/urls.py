from django.urls import path, include
from rest_framework.routers import SimpleRouter

from cats.views import CatViewSet
from cats.views import (cat_list, cat_detail, CatAPIView, CatAPIDetail,
                        CatList, CatDetail)

router = SimpleRouter()
router.register('api/v4/cats', CatViewSet)
# Если в классе queryset указан функцией, то в register нужно указать
# параметр basename.

urlpatterns = [
   path('api/v1/cats/', cat_list),
   path('api/v1/cat/<int:pk>/', cat_detail),
   path('api/v2/cats/', CatAPIView.as_view()),
   path('api/v2/cats/<int:pk>/', CatAPIDetail.as_view()),
   path('api/v3/cats/', CatList.as_view()),
   path('api/v3/cats/<int:pk>/', CatDetail.as_view()),

   path('', include(router.urls)),
   # path('cats/', ..., name='cat-list'),
   # path('cats/<int:pk>/', ..., name='cat-detail'),
]

