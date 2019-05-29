from django.conf.urls import url
from . import views

app_name = 'detection'

urlpatterns = [
    # url(r'/', views.homepage, name='homepage'),
    url(r'requirements/$', views.requirements, name='requirements')
]