from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Login en la raíz
    path('home/', views.home, name='home'),    # Página protegida después de login
]
