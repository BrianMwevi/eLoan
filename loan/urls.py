from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns =[
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('faqs', views.faqs, name="faqs"),
    path('profile/<int:pk>/', views.profile, name="profile"),
    path('lender', views.lenderpage, name="lenderpage"),
    
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)