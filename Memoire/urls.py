
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
   # path('', admin.site.urls),
    path('home/', include("home.urls")),
    path('contact/', include("contact.urls")),
    path('traitements/', include("traitements.urls")),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT) 