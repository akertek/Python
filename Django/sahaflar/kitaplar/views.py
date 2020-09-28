from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Kitap, Yazar


# Create your views here.


def index0(request):
    """
    mevcut n tane kitabı göstersin.
    altında bir form olsun, forma kitap aranabilsin.
    """

    return HttpResponse("index")

class IndexView(generic.ListView):
    # from django.views import generic
    # from .models import Kitap, Yazar
    template_name = "kitaplar/index.html"
    model = Kitap
    
    # context_object_name = "kitaplar"
    # template'de object_list yerine kitaplar kullanabilirim
    def get_queryset(self):
        # return super().get_queryset()
        return Kitap.objects.order_by("-yili")[:2]


def talep(request):
    """
    ziyaretçinin talep yapabileceği bir form bulunur.
    """

    return HttpResponse("talep")


def arama_sonuclari(request):
    """
    index'te yapılan aramaları gösterir
    """

    return HttpResponse("arama_sonuclari")
