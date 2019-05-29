from django.conf.urls import url
from . import views

app_name = 'detection'

urlpatterns = [
    # url(r'/', views.homepage, name='homepage'),
    url(r'^requirements/$', views.requirements, name='requirements'),
    url(r'^zip/$', views.zip, name='zip'),
    url(r'^get_files/$', views.get_files, name='get_files'),
]