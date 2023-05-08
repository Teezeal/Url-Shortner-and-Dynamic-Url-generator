from ctypes.wintypes import HINSTANCE
from wsgiref.validate import validator
from rest_framework import serializers

from shortner.helper import generate_short_url
from .models import Urls, Invoice

class UrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = ('id', 'original_url', 'short_url')
        read_only_fields = ('id', 'short_url')


    def create(self, validated_data):
        validated_data['short_url'] = generate_short_url(HINSTANCE)
        return Urls.objects.create(**validated_data)
    


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('id', 'customer_name','invoice_number', 'amount_due', 'paid', 'dynamic_url')





