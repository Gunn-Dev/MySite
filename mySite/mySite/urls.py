from django.contrib import admin
from django.urls import include
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('personal.urls')),
    path('blog/', include('blogpost.urls')),
]
