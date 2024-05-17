
from django.contrib import admin
from django.urls import path, include
from api.views import UserList

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/', include('api.urls')),
    path('api/user/', UserList.as_view(), name='user'),
]
