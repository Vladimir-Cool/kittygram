from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

from cats.views import (cat_list, cat_detail, CatAPIView, CatAPIDetail,
                        CatList, CatDetail, CatViewSet, OwnerViewSet,
                        LightCatViewSet)

router = SimpleRouter()
router.register('api/v4/cats', CatViewSet)
router.register('api/v4/owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet)
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

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

   # path('api-token-auth/', views.obtain_auth_token),

   # path('cats/', ..., name='cat-list'),
   # path('cats/<int:pk>/', ..., name='cat-detail'),
]

