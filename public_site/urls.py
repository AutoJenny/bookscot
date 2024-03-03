# This code snippet is from a Django project's URL configuration file (urls.py). Here's a breakdown of
# what it does:
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# This defines the URL patterns for the site. It maps URL paths to the 
# corresponding view functions in views.py that handle requests to those paths.

# The '' path maps to the home view function. name='home' allows referring to this path with the name 'home'.

# The 'directory/<int:directory_id>/' path includes a directory ID parameter 
# that gets passed to the directory_main_view view function. 

# The 'temp-directory-main/' path maps to the same view but without an ID parameter.

# The contact and submit-form paths map to the submit_form view. 

# The pages/<page>/ path allows accessing static pages by name. The page name gets 
# passed to the static_page view.
# This code snippet is defining URL patterns for a Django project. Each `path()` function call inside
# the `urlpatterns` list maps a URL path to a specific view function that will handle requests to that
# path. Here's a breakdown of what each path is doing:
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
