from django.contrib import admin
from django.urls import path
from pendaftaran import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login utama
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Navigasi utama
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tentang/', views.tentang, name='tentang'),
    path('chat/', views.chat, name='chat'),

    # Hotel CRUD
    path('hotel/', views.index, name='index'),
    path('hotel/tambah/', views.tambah, name='tambah'),
    path('hotel/edit/<int:id>/', views.edit, name='edit'),
    path('hotel/hapus/<int:id>/', views.hapus, name='hapus'),
]
