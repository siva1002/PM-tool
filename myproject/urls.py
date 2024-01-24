
from django.contrib import admin
from django.urls import path,include
from accounts.views import index, page1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index , name = 'index'),
    path('page1' ,page1  , name = 'page-1'),
    path('api/accounts/',include('accounts.urls')),
    path('api/management/',include('management.urls'))
]
