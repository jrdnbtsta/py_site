from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from photography.models import Img

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Img.objects.all().order_by("-date")[:25], template_name="photography/all_photos.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Img, template_name = 'photography/detail.html'))
]

