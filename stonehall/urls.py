import debug_toolbar
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include


from . import settings

urlpatterns = [
    path('', include('blog.urls')),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                      path('admin/', admin.site.urls),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
