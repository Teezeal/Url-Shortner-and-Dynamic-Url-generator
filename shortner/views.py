from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from django.shortcuts import redirect
from shortner.helper import generate_short_url
from .models import Urls
from .serializers import UrlsSerializer
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
    




   

