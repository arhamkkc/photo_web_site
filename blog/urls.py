from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name = 'home'),
    path('<int:id>',views.cat_detail,name = 'cat_detail'),
    path('gallery',views.gallery,name = 'gallery'),
    path('Contact',views.contact,name = 'contact'),
    path('about',views.about,name = 'about'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)