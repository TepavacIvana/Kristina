from django.db.migrations import serializer
from django.http import JsonResponse
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from rest_framework.views import APIView

from filmovi.models import Filmovi, Produkcija, Bioskopi
from filmovi.serializers import FilmoviSerializer, FilmoviProdukcijaSerializer, ProdukcijaSerializer, BioskopiSerializer
from rest_framework import generics, mixins, filters, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

# Create your views here.


class ProdukcijaList(generics.ListCreateAPIView):
    queryset = Produkcija.objects.all()
    serializer_class = ProdukcijaSerializer


class ProdukcijaDetail(generics.RetrieveAPIView):
    queryset = Produkcija.objects.all()
    serializer_class = ProdukcijaSerializer

    def myview(self, request):
        produkcijske_kuce = [obj.kuca for obj in Produkcija.objects.all()]
        return render(request, 'produkcija_template.html', {'produkcijske_kuce': produkcijske_kuce})


class BioskopiList(generics.ListCreateAPIView):
    queryset = Bioskopi.objects.all()
    serializer_class = BioskopiSerializer


class BioskopiDetail(generics.RetrieveAPIView):
    queryset = Bioskopi.objects.all()
    serializer_class = BioskopiSerializer

    def myview(self, request):
        bioskop = [obj.bio for obj in Bioskopi.objects.all()]
        return render(request, 'bioskopi_template.html', {'bioskop': bioskop})


class FilmoviList(generics.ListCreateAPIView):
    queryset = Filmovi.objects.all()
    serializer_class = FilmoviSerializer


class FilmoviDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Filmovi.objects.all()
    serializer_class = FilmoviSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class FilmoviBy(generics.ListAPIView):
    serializer_class = FilmoviSerializer

    def get_queryset(self):
        queryset = Filmovi.objects.filter(zanrovi=self.kwargs.get('zanr'))
        return queryset



