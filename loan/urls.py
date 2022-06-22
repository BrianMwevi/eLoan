from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns =[
    path('', views.home, name="home"),
    path('lender', views.lenderpage, name="lenderpage"),
    path('profile/<str:pk>', views.profile, name="profile"),
    # path('update_profile/<user_id>', views.update_profile, name="update_profile"),   
    
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)