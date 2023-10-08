from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Kulfiwala Admin"
admin.site.site_title = "Kulfiwala Admin Portal"
admin.site.index_title = "Welcome to Kulfiwala Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
