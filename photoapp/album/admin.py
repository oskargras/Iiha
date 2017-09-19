from django.contrib import admin
from album.models import Photo

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp']

    class Meta:
        model = Photo

admin.site.register(Photo, PhotoAdmin)