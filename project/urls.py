from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# path('recipes', include('recipes.urls_app')) // cria um subdominio
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls_app'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
