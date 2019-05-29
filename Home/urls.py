from django.conf.urls import url
from . import views

app_name = 'detection'

urlpatterns = [
    # url(r'/', views.homepage, name='homepage'),
    url(r'^requirements/$', views.requirements, name='requirements'),
    url(r'^get_files/$', views.get_files, name='get_files'),
    url(r'^get_status/$', views.get_status, name='get_status')
]