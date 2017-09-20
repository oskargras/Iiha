from django.shortcuts import render
from django.views import View
from album.models import Photo
from album.forms import PhotoForm
from django.views.generic import CreateView
from django.shortcuts import redirect
# Create your views here.


class HomeView(View):
    def get(self, request):
        queryset = Photo.objects.all()
        ctx = {"photos":queryset,}
        return render(request, "home.html", ctx)


class AddPhotoView(CreateView):
        model = Photo
        fields = ['image', 'description']
        success_url = '/'

        def form_valid(self, form):
            form.instance.user = self.request.user
            return super(AddPhotoView, self).form_valid(form)


class DelPhotoView(View):
    def get(self, request, photo_id):
        photo = Photo.objects.get(pk=photo_id)
        photo.delete()
        ctx = {"photo": photo}
        return redirect("/")

