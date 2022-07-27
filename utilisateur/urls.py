from django.urls import path,include
from .views import*
from rest_framework.urlpatterns import format_suffix_patterns

from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns=format_suffix_patterns([
    path('donateurm/', CreateDonateur.as_view(),name='registers-donateurm'),
    path('donateurorg/',CreateDonateurOr.as_view(),name='registers-donateurorg'),
    path('effectuerdo/',EffectuerDons.as_view(),name='registers-dons'),

    path('listonateur/<int:pk>', ListDonateur.as_view(),name='list-donateur'),
    path('list-don/<int:pk>',ListDon.as_view(),name='list-don'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
])