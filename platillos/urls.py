from django.conf.urls import url
from .views import PlatilloListView, PlatilloDeleteView, PlatilloCreateView, PlatilloDetailView, PlatilloUpdateView


urlpatterns = [
    url('^$', PlatilloListView.as_view(), name="list"),
    url('^(?P<pk>[0-9]+)/$', PlatilloDetailView.as_view(), name="detail"),
    url('^new/$', PlatilloCreateView.as_view(), name="create"),
    url('^delete/(?P<pk>[0-9]+)/$', PlatilloDeleteView.as_view(), name="delete"),
    url('^update/(?P<pk>[0-9]+)/$', PlatilloUpdateView.as_view(), name="edit")
]