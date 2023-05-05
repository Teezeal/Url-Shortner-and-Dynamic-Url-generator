from django.urls import path
from .views import UrlCreateView, UrlRedirectView
# from . import views 

urlpatterns = [
    path('create/', UrlCreateView.as_view(), name='url_create'),
    path('<str:short_url>/', UrlRedirectView.as_view(), name='url_redirect'),
    
]

