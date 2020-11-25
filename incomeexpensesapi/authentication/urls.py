from django.urls import path
from .views import RegisterView,VerifyEmail,LoginAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

# urlpatterns = [
#    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]


urlpatterns = [
    path('register/',RegisterView.as_view(),name="register"),
    path('login/',LoginAPIView.as_view(),name="login"),
    path('email-verify/',VerifyEmail.as_view(),name="email-verify"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
