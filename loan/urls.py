from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('faqs', views.faqs, name="faqs"),
    path('profile/<int:pk>/', views.profile, name="profile"),
    path('apply_loan/<user_id>/', views.apply_loan, name="apply_loan"),
    path('approve_loan/<borrower_id>/', views.approve_loan, name="approve_loan"),
    path('deposit/<user_id>', views.deposit, name="deposit"),

    path('lender', views.lenderpage, name="lenderpage"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
