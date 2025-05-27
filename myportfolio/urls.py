# myportfolio/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints remain unchanged
    path('api/', include('portfolio.urls')),

    # Auth routes: using Django built-in LoginView and LogoutView
    path('login/', auth_views.LoginView.as_view(template_name='portfolio/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # Frontend: landing/home page
    path('', TemplateView.as_view(template_name='portfolio/index.html'), name='home'),
]

# Static and media files for development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
