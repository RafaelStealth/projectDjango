from django.contrib import admin
from django.urls import include, path

# path('recipes', include('recipes.urls_app')) // cria um subdominio
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls_app'))

]
