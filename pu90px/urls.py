from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from pu90px import settings


urlpatterns = [
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path("", include("album.urls"), name='album-urls'),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls'))
]