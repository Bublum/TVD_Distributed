from django.conf.urls import url
from django.conf.urls.static import static

from TVD_Distributed import settings
from . import views

app_name = 'detection'

urlpatterns = [
    # url(r'/', views.homepage, name='homepage'),
    url(r'requirements/$', views.requirements, name='homepage'),
    url(r'get_files/$', views.get_files, name='get_files')
]