from django.conf.urls import url
from . import views

app_name = 'product_list'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
]