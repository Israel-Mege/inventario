from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.url')),  # Corrected typo (plural 'urls')
    path('docs/', include_docs_urls(title='Api Documentation')),
]
