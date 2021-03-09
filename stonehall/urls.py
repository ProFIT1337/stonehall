# from django.contrib import admin #comment in production
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from . import settings

urlpatterns = [
    # path('admin/', admin.site.urls), #comment in production
    path('', include('blog.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
