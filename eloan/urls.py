
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',include('loan.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

]
