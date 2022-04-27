from django.contrib import admin
from django.urls import path, include

from cakes import views
from .views import render_index_page
from .views import render_lk_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_index_page, name='render_index_page'),
    path('lk', render_lk_page, name='render_lk_page'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('auth/', include('django.contrib.auth.urls')),
]
