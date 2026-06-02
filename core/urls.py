from django.contrib import admin
from django.urls import path, include, re_path
from shop import views as shop_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('accounts/register/', shop_views.register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('shop.urls', namespace='shop')),
]

# Serve media files from local disk only when NOT using S3 storage
if not settings.USE_S3:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

# Static files are served by WhiteNoise in production; during development add static patterns
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
