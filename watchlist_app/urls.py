

from django.urls import path,include
from .views import WatchlistAV,WatchDetailAV,StreamPlatformAV,\
    StreamPlatformDetailAV,ReviewList,ReviewDetail,ReviewCreate
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream',StreamPlatformAV,basename='streamplatform')



urlpatterns = [
    path('list/',WatchlistAV.as_view()),
    path('list/<int:pk>/',WatchDetailAV.as_view(),name='movie-detail'),
    path('',include(router.urls)),
    # path('stream/',StreamPlatformAV.as_view()),
    path('stream/<int:pk>/',StreamPlatformDetailAV.as_view()),
    path('<int:pk>/review/',ReviewList.as_view()),
    path('<int:pk>/review-create/',ReviewCreate.as_view()),
    path('review/<int:pk>/',ReviewDetail.as_view()),
    path('api-auth',include('rest_framework.urls')),

    # path('review/',ReviewList.as_view(),name='review'),
    # path('review/<int:pk>/',ReviewDetail.as_view(),name='review'),

]