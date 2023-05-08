import random
import string
from rest_framework.views import APIView
from django.shortcuts import redirect
from shortner.helper import generate_short_url
from .models import Urls, Invoice
from .serializers import UrlsSerializer, InvoiceSerializer
from rest_framework import status
from rest_framework.response import Response





class UrlCreateView(APIView):
    def post(self, request):
        serializer = UrlsSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.save()

            url.short_url = generate_short_url(url.id)
            url.save()

            response_serializer = UrlsSerializer(url)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UrlRedirectView(APIView):
    def get(self, request, short_url):
        try:
            url = Urls.objects.get(short_url=short_url)
        except Urls.DoesNotExist:
            return Response({"error": "URL not found"}, status=status.HTTP_404_NOT_FOUND)
        return redirect(url.original_url)
    


class InvoiceDynamicUrlView(APIView):
    def post(self, request, invoice_id):
        try:
            invoice = Invoice.objects.get(id=invoice_id)
        except Invoice.DoesNotExist:
            return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)

        dynamic_url = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        invoice.dynamic_url = dynamic_url
        invoice.save()

        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)
    


class InvoiceDynamicUrlRedirectView(APIView):
    def get(self, request, invoice_id):
        invoice = Invoice.objects.get(id=id)
        if not invoice:
            return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)
        dynamic_url = invoice.dynamic_url
        return Response({'dynamic_url': dynamic_url})
    

# try:
#     invoice = Invoice.objects.get(id=invoice_id)
# except Invoice.DoesNotExist
# dynamic_url = invoice.dynamic_url


    








   

