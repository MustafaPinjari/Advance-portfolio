from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route for the homepage
    path('blog/', include('blog.urls', namespace='blog')),  # Add namespace here
    path('admin/', admin.site.urls),
   path('compiler/', include(('compiler.urls', 'compiler'), namespace='compiler')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
