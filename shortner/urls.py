from django.urls import path
from .views import InvoiceDynamicUrlView, UrlCreateView, UrlRedirectView,InvoiceDynamicUrlRedirectView


urlpatterns = [
    path('create/', UrlCreateView.as_view(), name='url_create'),
    path('<str:short_url>/', UrlRedirectView.as_view(), name='url_redirect'),
    path('invoices/<int:invoice_id>/dynamic-url/', InvoiceDynamicUrlView.as_view(), name='invoice_dynamic_url'),
    path('invoice/<int:id>/dynamic-url/', InvoiceDynamicUrlRedirectView.as_view(), name='invoice_dynamic_url'),
]

