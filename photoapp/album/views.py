from django.shortcuts import render
from django.views import View
from album.models import Photo

# Create your views here.


class HomeView(View):
    def get(self, request):
        queryset = Photo.objects.all()
        ctx = {"photos":queryset,}

        return render(request, "home.html", ctx)