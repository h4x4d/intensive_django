from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import Core.views

urlpatterns = [
    path('', include('homepage.urls')),
    path('catalog/', include('catalog.urls')),
    path('about/', include('about.urls')),
    path('feedback/', include('feedback.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]

handler404 = Core.views.NotFoundView.as_view()


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
