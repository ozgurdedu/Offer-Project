
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('offer.urls')),
    path('user/', include('user.urls')),
    path('question/', include('question.urls')),
    path('admin/', admin.site.urls),
   
]
