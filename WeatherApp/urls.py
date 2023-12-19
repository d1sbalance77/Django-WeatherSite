from django.contrib import admin
from django.urls import path,include
from weather.views import MyLoginView, logout_view
import weather.views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls'), name='WeatherMainPage'),
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

