from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# path('recipes', include('recipes.urls_app')) // cria um subdominio
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls_app')),
    path('authors/', include('authors.urls_app')),

]

# Adiciona rotas estáticas para os arquivos de mídia (media files) ao conjunto de padrões de URL do projeto.
# Isso permite que os arquivos de mídia sejam acessados através de URLs no navegador durante o desenvolvimento,
# mesmo quando o servidor de desenvolvimento do Django está em execução.
# 'settings.MEDIA_URL' é a URL base para os arquivos de mídia, e 'settings.MEDIA_ROOT' é o diretório no sistema de arquivos
# onde os arquivos de mídia são armazenados.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
