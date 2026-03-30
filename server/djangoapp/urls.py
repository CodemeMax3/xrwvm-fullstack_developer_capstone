from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # login
    path('login', views.login_user, name='login'),

    # logout
    path('logout', views.logout_request, name='logout'),

    # registration
    path('register', views.registration, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)