from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('directory/<int:directory_id>/', views.directory_main_view, name='directory_main_view'),
    path('temp-directory-main/', views.directory_main_view, name='temp_directory_main'),
    path('pages/contact/', views.submit_form, name='contact'),
    path('submit-form/', views.submit_form, name='submit_form'),
    path('pages/<page>/', views.static_page, name='static_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
