from django.conf.urls import url
from . import views
# Create your views here.

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
