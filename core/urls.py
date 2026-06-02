import os
from django.contrib import admin
from django.urls import path, include, re_path
from shop import views as shop_views
from django.conf import settings
from django.conf.urls.static import static
from django.http import FileResponse, Http404
from django.views.generic.base import RedirectView


def media_serve(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if not os.path.exists(file_path):
        raise Http404
    return FileResponse(open(file_path, 'rb'))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('accounts/register/', shop_views.register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('shop.urls', namespace='shop')),
]

if not settings.USE_S3:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', media_serve),
    ]

if True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
