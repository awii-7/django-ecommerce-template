import statistics
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Ebazar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
